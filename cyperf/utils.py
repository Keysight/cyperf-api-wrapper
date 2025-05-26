import os
import socket
import time
import datetime
import warnings
from pprint import pprint
import sys
import cyperf


def format_warning_cli_issues(message, category, filename, lineno=None, line=None):
    return f"{category.__name__}: {message}\n"


warnings.formatwarning = format_warning_cli_issues


class TestRunner:
    """Convenience class for common test run operations"""

    def __init__(self, controller, username="", password="", refresh_token="", license_server=None, license_user="", license_password=""):
        self.controller = controller
        self.host = f'https://{controller}'
        self.license_server   = license_server
        self.license_user     = license_user
        self.license_password = license_password

        self.configuration            = cyperf.Configuration(host=self.host,
                                                             refresh_token=refresh_token,
                                                             username=username,
                                                             password=password)
        self.configuration.verify_ssl = False
        self.api_client               = cyperf.ApiClient(self.configuration)
        self.added_license_servers    = []

        self.update_license_server()

        self.agents = {}
        agents_api  = cyperf.AgentsApi(self.api_client)
        self.available_agents = agents_api.get_agents(exclude_offline='true')
        for agent in self.available_agents:
            self.agents[agent.ip] = agent

    def __del__(self, time=time, datetime=datetime):
        if 'time' not in sys.modules or not sys.modules['time']:
            sys.modules['time'] = time
        self.remove_license_server()

    def update_license_server(self):
        if not self.license_server or self.license_server == self.controller:
            return
        license_api = cyperf.LicenseServersApi(self.api_client)
        try:
            response = license_api.get_license_servers()
            for lServerMetaData in response:
                if lServerMetaData.host_name == self.license_server:
                    if 'ESTABLISHED' == lServerMetaData.connection_status:
                        pprint(f'License server {self.license_server} is already configured')
                        return
                    license_api.delete_license_server(str(lServerMetaData.id))
                    waitTime = 5 # seconds
                    print(f'Waiting for {waitTime} seconds for the license server deletion to finish.')
                    time.sleep(5)
                    break
                    
            lServer = cyperf.LicenseServerMetadata(host_name=self.license_server,
                                                   trust_new=True,
                                                   user=self.license_user,
                                                   password=self.license_password)
            print(f'Configuring new license server {self.license_server}')
            newServers = license_api.create_license_servers(license_server_metadata=[lServer])
            while newServers:
                for server in newServers:
                    s = license_api.get_license_server_by_id(
                        str(server.id))
                    if 'IN_PROGRESS' != s.connection_status:
                        newServers.remove(server)
                        self.added_license_servers.append(server)
                        if 'ESTABLISHED' == s.connection_status:
                            print(f'Successfully added license server {s.host_name}')
                        else:
                            raise Exception(f'Could not connect to license server {s.host_name}')
                time.sleep(0.5)
        except cyperf.ApiException as e:
            raise (e)

    def remove_license_server(self):
        license_api = cyperf.LicenseServersApi(self.api_client)
        for server in self.added_license_servers:
            try:
                license_api.delete_license_server(str(server.id))
            except cyperf.ApiException as e:
                pprint(f'{e}')

    def load_configuration_files(self, configuration_files=[]):
        config_api = cyperf.ConfigurationsApi(self.api_client)
        config_ops = []
        for config_file in configuration_files:
            config_ops.append(config_api.start_configs_import(config_file))

        configs = []
        for op in config_ops:
            try:
                results = op.await_completion()
                configs += [(elem['id'], elem['configUrl']) for elem in results]
            except cyperf.ApiException as e:
                raise (e)
        return configs

    def load_configuration_file(self, configuration_file):
        configs = self.load_configuration_files([configuration_file])
        if configs:
            return configs[0]
        else:
            return None

    def remove_configurations(self, configurations_ids=[]):
        config_api = cyperf.ConfigurationsApi(self.api_client)
        for config_id in configurations_ids:
            config_api.delete_config(config_id)

    def remove_configuration(self, configurations_id):
        self.remove_configurations([configurations_id])

    def create_session_by_config_name(self, config_name):
        configsApiInstance = cyperf.ConfigurationsApi(self.api_client)
        appMixConfigs      = configsApiInstance.get_configs(search_col='displayName', search_val=config_name)
        if not len(appMixConfigs):
            return None

        return self.create_session(appMixConfigs[0].config_url)

    def create_session(self, config_url):
        session_api        = cyperf.SessionsApi(self.api_client)
        session            = cyperf.Session()
        session.config_url = config_url
        sessions           = session_api.create_sessions([session])
        if len(sessions):
            return sessions[0]
        else:
            return None

    def delete_session(self, session):
        session_api = cyperf.SessionsApi(self.api_client)
        test        = session_api.get_session_test(session_id=session.id)
        if test.status != 'STOPPED':
            self.stop_test(session)
        session_api.delete_session(session.id)

    def assign_agents(self, session, agent_map=None, augment=False, auto_assign=False):
        # Assing agents to the indivual network segments based on the input provided
        for net_profile in session.config.config.network_profiles:
            for ip_net in net_profile.ip_network_segment:
                if agent_map and ip_net.name not in agent_map:
                    continue
                if auto_assign and self.agents:
                    agent_ip = next(iter(self.agents))
                    agents = [self.agents.pop(agent_ip)]
                elif self.agents:
                    mapped_ips = agent_map[ip_net.name]
                    agents = [self.agents[ip]
                              for ip in mapped_ips
                              if ip in self.agents]
                    for agent in agents:
                        del self.agents[agent.ip]
                else:
                    raise ValueError("Insufficient agents found on setup.")
                agent_details = [cyperf.AgentAssignmentDetails(agent_id=agent.id, id = str(idx))
                                 for agent, idx in zip(agents, range(len(agents)))]
                if not ip_net.agent_assignments:
                    ip_net.agent_assignments = cyperf.AgentAssignments(ByID=[], ByTag=[])

                if augment:
                    ip_net.agent_assignments.by_id.extend(agent_details)
                else:
                    ip_net.agent_assignments.by_id = agent_details
                ip_net.update()

    def disable_automatic_network(self, session):
        for net_profile in session.config.config.network_profiles:
            for ip_net in net_profile.ip_network_segment:
                ip_net.ip_ranges[0].ip_auto = False
                ip_net.update()

    def add_apps(self, session, appNames):
        # Retrieve the app from precanned Apps
        resource_api = cyperf.ApplicationResourcesApi(self.api_client)
        app_info     = []
        for appName in appNames:
            apps    = resource_api.get_resources_apps(search_col='Name', search_val=appName)
            if not len(apps):
                print('Couldn\'t find any {appName} app.')
                raise Exception(f'Couldn\'t find \'{appName}\' app')

            # Add the app to the App-Mix, which may be empty until now.
            app_info.append(cyperf.Application(external_resource_url=apps[0].id, objective_weight=1))

        if not session.config.config.traffic_profiles:
            session.config.config.traffic_profiles.append(cyperf.ApplicationProfile(name="Application Profile"))
            session.config.config.traffic_profiles.update()
        
        app_profile = session.config.config.traffic_profiles[0]
        for app in app_info:
            app_profile.applications.append(app)
            
        app_profile.applications.update()

    def add_app(self, session, appName):
        self.add_apps(session, [appName])

    def set_objective_and_timeline(self, session,
                                   objective_type=cyperf.ObjectiveType.SIMULATED_USERS,
                                   objective_unit=cyperf.ObjectiveUnit.EMPTY,
                                   objective_value=100,
                                   test_duration=600):
        primary_objective = session.config.config.traffic_profiles[0].objectives_and_timeline.primary_objective
        primary_objective.type = objective_type
        primary_objective.unit = objective_unit
        primary_objective.update()

        for segment in primary_objective.timeline:
            if segment.enabled and (segment.segment_type == cyperf.SegmentType.STEADYSEGMENT or segment.segment_type == cyperf.SegmentType.NORMALSEGMENT):
                segment.duration        = test_duration
                segment.objective_value = objective_value
                segment.objective_unit  = objective_unit
        primary_objective.update()

    def start_test(self, session):
        test_ops_api  = cyperf.TestOperationsApi(self.api_client)
        test_start_op = test_ops_api.start_test_run_start(session_id=session.id)
        try:
            test_start_op.await_completion()
        except cyperf.ApiException as e:
            raise (e)

    def wait_for_test_stop(self, session, test_monitor=None):
        session_api      = cyperf.SessionsApi(self.api_client)
        monitored_at     = None
        wait_interval    = 0.5
        while 1:
            test = session_api.get_session_test(session_id=session.id)
            if 'STOPPED' == test.status:
                break
            if test_monitor:
                if monitored_at:
                    monitor_start = monitored_at + 1
                else:
                    monitor_start = 0
                monitor_upto      = monitor_start - 1 # Anything less than monitor_start will mean up to most latest
                monitored_at      = test_monitor(test, monitor_start, monitor_upto)
            time.sleep(wait_interval)

    def stop_test(self, session):
        test_ops_api = cyperf.TestOperationsApi(self.api_client)
        test_stop_op = test_ops_api.start_test_run_stop(session_id=session.id)
        try:
            test_stop_op.await_completion()
        except cyperf.ApiException as e:
            raise (e)

    def collect_stats(self, test, stats_name, time_from, time_to, stats_processor=None):
        stats_api = cyperf.StatisticsApi(self.api_client)
        stats     = stats_api.get_result_stats(test.test_id)
        stats     = [stat for stat in stats if stats_name in stat.name]
        if time_from:
            if time_to > time_from:
                stats = [stats_api.get_result_stat_by_id(test.test_id, stat.name, var_from=time_from, to=time_to) for stat in stats]
            else:
                stats = [stats_api.get_result_stat_by_id(test.test_id, stat.name, var_from=time_from) for stat in stats]
        else:
            stats     = [stats_api.get_result_stat_by_id(test.test_id, stat.name) for stat in stats]
        if stats_processor:
            stats = stats_processor(stats)

        return stats

    def format_milliseconds(self, milliseconds):
        seconds = int(milliseconds / 1000) % 60
        minutes = int(milliseconds / (1000 * 60)) % 60
        hours   = int(milliseconds / (1000 * 60 * 60)) % 24

        return f'{hours:02d}H:{minutes:02d}M:{seconds:02d}S'

    def is_valid_ipv4(ip):
        try:
            socket.inet_aton(ip)
        except Exception:
            return False
        return True

    def is_valid_ipv6(ip):
        try:
            socket.inet_pton(socket.AF_INET6, ip)
        except Exception:
            return False
        return True

    def format_stats_dict_as_table(self, stats_dict={}):
        if not stats_dict:
            return

        stat_names = stats_dict.keys()
        col_widths = [max(len(str(val)) + 2 for val in val_list + [stat_name]) for stat_name, val_list in stats_dict.items()]
        header     = '|'.join([f'{name:^{col_width}}' for name, col_width in zip(stat_names, col_widths)])
        line_delim = '+'.join(['-' * col_width for col_width in col_widths])

        lines = ['|'.join([f'{val:^{col_width}}' for val, col_width in zip(item, col_widths)]) for item in zip(*stats_dict.values())]
        return [line_delim, header, line_delim] + lines + [line_delim]


def parse_cli_options(extra_options=[]):
    """Can be used to get parameters from the CLI or env vars that are broadly useful for CLI tests"""
    import argparse

    parser = argparse.ArgumentParser(description='A simple UDP test')
    parser.add_argument('--controller', help='The IP address or the hostname of the CyPerf controller', required=True)
    parser.add_argument('--user', help='The username for accessing the controller, needs a password too')
    parser.add_argument('--password', help='The password for accessing the controller, needs a username too')
    parser.add_argument('--license-server', help='The IP address or the hostname of the license server, default is the controller')
    parser.add_argument('--license-user', help='The username for accessing the license server, needed if controller is not the license server')
    parser.add_argument('--license-password', help='The password for accessing the license server, needed if controller is not the license server')
    for option, help, required in extra_options:
        parser.add_argument(option, help=help, required=required)
    args = parser.parse_args()

    if not args.license_server or args.license_server == args.controller:
        args.license_server   = args.controller
        args.license_user     = None
        args.license_password = None
    else:
        if not args.license_user or not args.license_password:
            parser.error('--license-user and --license-password are mandatory if a different --license-server is provided')

    if args.user and args.password:
        offline_token = None
    else:
        if args.user or args.password:
            warnings.warn('Onlye one of --user and --password is provided, looking for offline token')

        try:
            offline_token = os.environ['CYPERF_OFFLINE_TOKEN']
        except KeyError as e:
            parser.error(f'Couldn\'t find environment variable {e}')

    return args, offline_token


def create_api_client_cli(verify_ssl=True):
    """Parse the args passed to the current script and use them to create an API client; optionally disable SSL verification"""
    cli_args, offline_token = parse_cli_options()
    host = f'https://{cli_args.controller}'
    
    configuration            = cyperf.Configuration(host=host,
                                                    refresh_token=offline_token,
                                                    username=cli_args.user,
                                                    password=cli_args.password)
    configuration.verify_ssl = verify_ssl
    return cyperf.ApiClient(configuration)
