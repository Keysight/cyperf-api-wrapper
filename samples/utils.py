import os
import socket
import time
import datetime
import warnings
from pprint import pprint
import sys
import cyperf
import json
import pyshark
import asyncio
import math
from urllib.parse import urlparse

def extract_path(url):
    parsed_url = urlparse(url)
    return parsed_url.path

def extract_last_part_of_path(url):
    parsed_url = urlparse(url)
    return os.path.basename(parsed_url.path)

def turns_coversations_dict_values(input_dict):
    # Use dictionary comprehension to create a new dictionary with the updated values
    updated_dict = {key: math.ceil(value / 2) for key, value in input_dict.items()}
    return updated_dict

def udp_identify_client_server(pcap_file):
    
    
    # Create a pyshark Capture object
    capture = pyshark.FileCapture(pcap_file, display_filter='udp')
        # Initialize an empty dictionary to store the client-server information for each TCP stream
    client_server_info = {}

    # Iterate through all packets in the capture
    for packet in capture:
        # Extract the TCP stream index
        stream_index = packet.udp.stream
        
        # Check if the packet is a SYN packet (i.e., the start of a new TCP connection)
        #if packet.tcp.flags_syn == 'True' and packet.tcp.flags_ack == 'False':
            
        # If the stream index is not already in the dictionary, add it with the client-server information
        if stream_index not in client_server_info:
                client_server_info[stream_index] = {
                    'client_ip': packet.ip.src,
                    'server_ip': packet.ip.dst
                }
             
    # Close the capture
    capture.close()

    return client_server_info

def identify_client_server(pcap_file):
    # Create a pyshark Capture object
    capture = pyshark.FileCapture(pcap_file, display_filter='tcp')

    # Initialize an empty dictionary to store the client-server information for each TCP stream
    client_server_info = {}

    # Iterate through all packets in the capture
    for packet in capture:
        # Extract the TCP stream index
        stream_index = packet.tcp.stream
        
        if ((packet.tcp.flags_syn == '1')  and (packet.tcp.flags_ack == '0' )):
            
            # If the stream index is not already in the dictionary, add it with the client-server information
            if stream_index not in client_server_info:
                client_server_info[stream_index] = {
                    'client_ip': packet.ip.src,
                    'server_ip': packet.ip.dst
                }
            
    # Close the capture
    capture.close()
    return client_server_info

def udp_count_byte_direction_changes_sync(pcap_file):

    conversation_per_udp_stream = {}

    # Create a pyshark Capture object
    capture = pyshark.FileCapture(pcap_file, display_filter='udp')

    udp_packet_count_per_stream = {}

    # Initialize a dictionary to store the byte direction change count for each TCP stream
    udp_byte_direction_changes = {}

    # Initialize a dictionary to store the previous packet direction for each TCP stream
    previous_packet_direction = {}
    
    # Initialize an empty dictionary to store the client-server information for each TCP stream
    udp_client_server_info = udp_identify_client_server(pcap_file)

    # Iterate through all packets in the capture
    for packet in capture:
        
        # Extract the TCP stream index
        stream_index = packet.udp.stream
        
        # Initialize the byte direction change count for this stream if it doesn't exist
        if stream_index not in udp_byte_direction_changes:
            udp_byte_direction_changes[stream_index] = 0

        # Initialize the UDP packet count for this stream if it doesn't exist
        if stream_index not in udp_packet_count_per_stream:
            udp_packet_count_per_stream[stream_index] = 0

        # Increment the UDP packet count for this stream
        udp_packet_count_per_stream[stream_index] += 1

        # Check if the packet is in the forward direction (i.e., from client to server)
        if packet.ip.src == udp_client_server_info[stream_index]['client_ip']:
            current_direction = 'forward'
        else:
            current_direction = 'reverse'

        # Check if the previous packet direction is different from the current packet direction
        if stream_index in previous_packet_direction and previous_packet_direction[stream_index] != current_direction:
            udp_byte_direction_changes[stream_index] += 1

        # Update the previous packet direction for this stream
        previous_packet_direction[stream_index] = current_direction
       
    # Close the capture
    capture.close()
    
    for stream in udp_packet_count_per_stream:
            if ( udp_byte_direction_changes[stream] == 0 ):
                  conversation_per_udp_stream[ stream]= udp_packet_count_per_stream[stream] - (udp_byte_direction_changes[stream])
            if ( udp_byte_direction_changes[stream] == 1 ):
                  conversation_per_udp_stream[ stream]= udp_packet_count_per_stream[stream] - (udp_byte_direction_changes[stream])
            if ( udp_byte_direction_changes[stream] > 1 ):
                  conversation_per_udp_stream[ stream]= udp_packet_count_per_stream[stream] - (udp_byte_direction_changes[stream] - 1 )
    return conversation_per_udp_stream

def count_byte_direction_changes_sync(pcap_file):
    # Create a pyshark Capture object
    capture = pyshark.FileCapture(pcap_file, display_filter='tcp && tcp.payload != ""')

    # Initialize a dictionary to store the byte direction change count for each TCP stream
    byte_direction_changes = {}

    # Initialize a dictionary to store the previous packet direction for each TCP stream
    previous_packet_direction = {}
    
    # Initialize an empty dictionary to store the client-server information for each TCP stream
    client_server_info = identify_client_server(pcap_file)
    
    # Iterate through all packets in the capture
    for packet in capture:
        
        # Extract the TCP stream index
        stream_index = packet.tcp.stream
        
        # Initialize the byte direction change count for this stream if it doesn't exist
        if stream_index not in byte_direction_changes:
            byte_direction_changes[stream_index] = 0
           
        # Check if the packet is in the forward direction (i.e., from client to server)
        if packet.ip.src == client_server_info[stream_index]['client_ip']:
            current_direction = 'forward'
        else:
            current_direction = 'reverse'

        # Check if the previous packet direction is different from the current packet direction
        if stream_index in previous_packet_direction and previous_packet_direction[stream_index] != current_direction:
            byte_direction_changes[stream_index] += 1

        # Update the previous packet direction for this stream
        previous_packet_direction[stream_index] = current_direction

    # Close the capture
    capture.close()

    return byte_direction_changes

async def count_udp_conversations(pcap_file):
    # Run the synchronous code in a separate thread
    loop = asyncio.get_running_loop()
    conversation_count = await loop.run_in_executor(None, udp_count_byte_direction_changes_sync, pcap_file)
    return conversation_count   

async def count_tcp_conversations(pcap_file):
    # Run the synchronous code in a separate thread
    loop = asyncio.get_running_loop()
    conversation_count = await loop.run_in_executor(None, count_byte_direction_changes_sync, pcap_file)
    return conversation_count



def prepare_payload(json_string,item):
    # Example  JSON string
    #json_string = '{"AppName":"Custom application Mar 14 2025 01:12","Actions":[{"Name":"Action 1","Captures":[{"CaptureId":"68","Flows":[{"AppFlowId":"all","Exchange":[]}]}]}]}'

    # Load the JSON string into a Python dictionary
    data = json.loads(json_string)

    new_app_name = "CCA-"+ item[0].rsplit('.', 1)[0]
    c_id         = item[1]

    # Substitute AppName in the dictionary
    data['AppName'] = new_app_name
    data['Actions'][0]['Captures'][0]['CaptureId'] = c_id

    # Convert the dictionary back to a JSON string
    new_json_string = json.dumps(data)

    return new_json_string


def format_warning_cli_issues(message, category, filename, lineno=None, line=None):
    return f"{category.__name__}: {message}\n"


warnings.formatwarning = format_warning_cli_issues


class Utils:
    WAP_CLIENT_ID = 'clt-wap'

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

        self.resource_api             = cyperf.ApplicationResourcesApi(self.api_client)
        
        self.update_license_server()

        self.agents = {}
        agents_api  = cyperf.AgentsApi(self.api_client)
        agents      = agents_api.get_agents()
        for agent in agents:
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
                    license_api.delete_license_servers(str(lServerMetaData.id))
                    waitTime = 5 # seconds
                    print(f'Waiting for {waitTime} seconds for the license server deletion to finish.')
                    time.sleep(5) # How can I avoid this sleep????
                    break
                    
            lServer = cyperf.LicenseServerMetadata(host_name=self.license_server,
                                                   trust_new=True,
                                                   user=self.license_user,
                                                   password=self.license_password)
            print(f'Configuring new license server {self.license_server}')
            newServers = license_api.create_license_servers(license_server_metadata=[lServer])
            while newServers:
                for server in newServers:
                    s = license_api.get_license_servers_by_id(
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
                license_api.delete_license_servers(str(server.id))
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
            config_api.delete_configs(config_id)

    def remove_configuration(self, configurations_id):
        self.remove_configurations([configurations_id])

    def create_session_by_config_name(self,configName ):
        configsApiInstance = cyperf.ConfigurationsApi(self.api_client)
        appMixConfigs      = configsApiInstance.get_configs(search_col='displayName', search_val=configName)
        if not len(appMixConfigs):
            return None

        return self.create_session(appMixConfigs[0].config_url)

    def create_session(self, config_url):
        session_api        = cyperf.SessionsApi(self.api_client)
        session            = cyperf.Session()
        session.config_url = config_url
        sessions           = session_api.create_sessions([session])
        if len(sessions):
            print( type(sessions))
            print( type(sessions[0]))
            return sessions[0]
        else:
            return None

    def delete_session(self, session):
        session_api = cyperf.SessionsApi(self.api_client)
        test        = session_api.get_session_test(session_id=session.id)
        if test.status != 'STOPPED':
            self.stop_test(session)
        session_api.delete_session(session.id)

    def assign_agents(self, session, agent_map, augment=False):
        # Assing agents to the indivual network segments based on the input provided
        for net_profile in session.config.config.network_profiles:
            for ip_net in net_profile.ip_network_segment:
                if ip_net.name in agent_map:
                    mapped_ips    = agent_map[ip_net.name]
                    agent_details = [cyperf.AgentAssignmentDetails(agent_id=self.agents[agent_ip].id, id = self.agents[agent_ip].id) for agent_ip in mapped_ips if agent_ip in self.agents] # why do we need to pass agent_id and id both????
                    if not ip_net.agent_assignments:
                        ip_net.agent_assignments = cyperf.AgentAssignments(ByID=[], ByTag=[]) # Why is ByTag argument a must????

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
        app_profile.applications += app_info
        app_profile.active = True
        app_profile.update()
        app_profile.applications.update()
        

    def get_apps(self, session,):
        resource_api = cyperf.ApplicationResourcesApi(self.api_client)
        cyperf_apps=[]
        try:
            api_response = resource_api.get_resources_apps()
            print("The response of ApplicationResourcesApi->get_resources_apps:\n")
            for index in range(len(api_response)):
                cyperf_apps.append(api_response[index].name)
            #Process individual AppNames to get more common names 
            return cyperf_apps
        except Exception as e:
            print("Exception when calling ApplicationResourcesApi->get_resources_apps: %s\n" % e)
        


    def add_apps_with_weights(self, session, app_dict):
        resource_api = cyperf.ApplicationResourcesApi(self.api_client)
        app_info     = []
        for appName in app_dict.keys():
            apps    = resource_api.get_resources_apps(search_col='Name', search_val=appName)
            if not len(apps):
                print('Couldn\'t find any {appName} app.')
                raise Exception(f'Couldn\'t find \'{appName}\' app')

            app_info.append(cyperf.Application(external_resource_url=apps[0].id, objective_weight=7))
          
        if not session.config.config.traffic_profiles:
            session.config.config.traffic_profiles.append(cyperf.ApplicationProfile(name="Application Profile"))
            session.config.config.traffic_profiles.update()
        
        app_profile = session.config.config.traffic_profiles[0]
        
        #It is very imprtant to forcefully upadate the application Profile 
        app_profile.active = True
        app_profile.update()
        #Now update the applications . The Order of update is very important . You must always update the parent , then you must update the child 
        #The update in no capacity is recursive as of now . It may be in future - we do not know . 
        app_profile.applications.extend(app_info)
        app_profile.applications.update()
        
        #Update the weights of the individual application 
        for appName in app_dict:

            apps    = resource_api.get_resources_apps(search_col='Name', search_val=appName)
            if not len(apps):
                print('Couldn\'t find any {appName} app.')
                raise Exception(f'Couldn\'t find \'{appName}\' app')
                   
            for i in range(len(app_profile.applications)):
                
                if((app_profile.applications[i].name).lower() == appName.lower()):
                    app_profile.applications[i].objective_weight=app_dict[appName]
                    app_profile.applications[i].update()
                    break

    def get_session(self,session):
        session_api      = cyperf.SessionsApi(self.api_client)
        return session_api.get_session_by_id(session.id)
        

    def get_apps(self, session,):
        resource_api = cyperf.ApplicationResourcesApi(self.api_client)
        cyperf_apps=[]
        try:
            api_response = resource_api.get_resources_apps()
            #print("The response of ApplicationResourcesApi->get_resources_apps:\n")
            for index in range(len(api_response)):
                cyperf_apps.append(api_response[index].name)
           
            return cyperf_apps
        except Exception as e:
            print("Exception when calling ApplicationResourcesApi->get_resources_apps: %s\n" % e)
        
    def add_app(self, session, appName):
        self.add_apps(session, [appName])
    
    #new function
    async def upload_the_capture_file(self, pcap_file):
        #validate the pcap first
        #turns - means the numbe rof times the direction of bytes changes in a TCP stream .
        turns_per_stream= await count_tcp_conversations(pcap_file)
        udp_conversations_per_stream= await count_udp_conversations(pcap_file)
        #update the value in the dictionary such that turns are replaced by conversations for each tcp stream . The UDP part is taken care .
        conversation_per_stream=turns_coversations_dict_values(turns_per_stream)
      
        #Total Number of TCP coversations / exchanges - Summation across all streams 
        total_number_of_conversations=sum(value for value in conversation_per_stream.values())
        
        #Total Number of UDP coversations / exchanges - Summation across all streams
        udp_total_number_of_conversations = sum(value for value in udp_conversations_per_stream.values())

        if( total_number_of_conversations > 0 ):
            print("\nThe number of tcp conversation for the file {} is {}".format((os.path.basename(pcap_file)),total_number_of_conversations))
        if(udp_total_number_of_conversations > 0 ):
            print("\nThe number of udp conversation for the file {} is {}".format((os.path.basename(pcap_file)), udp_total_number_of_conversations))

        if ((total_number_of_conversations + udp_total_number_of_conversations) > 10000):
             print(f"The pcap file - {pcap_file} has more than 10000 exchanges/ conversations and this is not suppoted by CyPerf. \n The max number of converstaions supported in 10000.\n This file will be skipped !")
             return
        #if (udp_total_number_of_conversations > 10000):
             #print(f"The pcap file - {pcap_file} has more than 10000 exchanges/ conversations and this is not suppoted by CyPerf. \n The max number of converstaions supported in 10000.\n This file will be skipped !")
             #return
        print(f"\nStarting upload of capture file-{os.path.basename(pcap_file)} to CyPerf Resouce Library.")
        
        response =self.resource_api.start_resources_captures_upload_file( pcap_file)
        
        flag = True
        
        while flag:
            res = self.resource_api.poll_resources_captures_upload_file(upload_file_id=str(response.id),_request_timeout=300)
            if res.state == "SUCCESS":
                print("File {} is uploaded SUCCESSFULLY!!.\n".format(os.path.basename(pcap_file)))
                flag = False    
            else: 
                print("Uploading file {} is {}".format(os.path.basename(pcap_file),res.state))
                time.sleep(3)
        
    def create_apps_from_captures(self):
        list_of_captures              =  self.resource_api.get_resources_captures()
        user_uploaded_list_of_captures =  [ (x.name,x.id) for x in list_of_captures if x.owner_id!='system']
        for item in user_uploaded_list_of_captures:
            #create the json payload
            json_string = '{"AppName":"Custom","Actions":[{"Name":"Super-Action","Captures":[{"CaptureId":"00","Flows":[{"AppFlowId":"all","Exchange":[]}]}]}]}'
            pp=prepare_payload(json_string,item)
            #import pdb;pdb.set_trace()
            flag = True
            create_app_operation_instance = cyperf.CreateAppOperation.from_json(pp)
            response=self.resource_api.start_resources_create_app(create_app_operation_instance)
            while flag:
                res = self.resource_api.poll_resources_create_app(id=response.id,_request_timeout=300)
                if res.state == "SUCCESS":
                    print("App from {} is created SUCCESSFULLY!!.\n".format(item[0]))
                    flag = False    
                else: 
                    print("App from {} - creation is {}".format(item[0],res.state))
                    time.sleep(1)
        return True



    def set_objective_and_timeline(self, session,
                                   objective_type=cyperf.ObjectiveType.SIMULATED_USERS,
                                   objective_unit=cyperf.ObjectiveUnit.EMPTY,
                                   objective_value=100,
                                   test_duration=600):
        primary_objective = session.config.config.traffic_profiles[0].objectives_and_timeline.primary_objective
        primary_objective.type = objective_type
        primary_objective.unit = objective_unit
        primary_objective.update() # How will the customer know that update() has to be called twice (separately)????

        for segment in primary_objective.timeline: # How will the customer know that primary_objective.timeline has to be updated instead of objectives_and_timeline.timeline_segments????
            if segment.enabled and (segment.segment_type == cyperf.SegmentType.STEADYSEGMENT or segment.segment_type == cyperf.SegmentType.NORMALSEGMENT):
                segment.duration        = test_duration
                segment.objective_value = objective_value
                segment.objective_unit  = objective_unit
        primary_objective.update()
        #import pdb;pdb.set_trace()

    def start_test(self, session):
        test_ops_api  = cyperf.TestOperationsApi(self.api_client)
        test_start_op = test_ops_api.start_start_traffic(session_id=session.id)
        try:
            test_start_op.await_completion()
        except cyperf.ApiException as e:
            raise (e) # The error shown in the GUI is not sent back to the API caller, why????

    def wait_for_test_stop(self, session, test_monitor=None):
        session_api      = cyperf.SessionsApi(self.api_client)
        monitored_at     = None
        wait_interval    = 0.5
        while 1:
            test = session_api.get_test(session_id=session.id)
            if 'STOPPED' == test.status: # Why don't we have a enum here????
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
        test_stop_op = test_ops_api.start_stop_traffic(session_id=session.id)
        try:
            test_stop_op.await_completion()
        except cyperf.ApiException as e:
            raise (e)

    def collect_stats(self, test, stats_name, time_from, time_to, stats_processor=None):
        stats_api = cyperf.StatisticsApi(self.api_client)
        stats     = stats_api.get_stats(test.test_id)
        stats     = [stat for stat in stats if stats_name in stat.name]
        if time_from:
            if time_to > time_from:
                stats = [stats_api.get_stats_by_id(test.test_id, stat.name, var_from=time_from, to=time_to) for stat in stats]
            else:
                stats = [stats_api.get_stats_by_id(test.test_id, stat.name, var_from=time_from) for stat in stats]
        else:
            stats     = [stats_api.get_stats_by_id(test.test_id, stat.name) for stat in stats]
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

    def search_configuration_file(self, name):
        try:
            flag=0
            api_instance = cyperf.ConfigurationsApi(self.api_client)
            api_response = api_instance.get_configs()
            while(api_response):
                dn=api_response.pop().to_dict()['displayName']
                if (dn == name):
                    print (f"The configuration was found and it will be loaded now ")
                    flag =1 
                    return True
            if (flag==0):
                print (f"The configuration was not found and it will be not be loaded.Provide an existing configuration name ")
                return False
        except Exception as e:
            print("Exception when calling ConfigurationsApi->get_configs: %s\n" % e)


def parse_cli_options(extra_options=[]):
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
            warnings.warn('Only one of --user and --password is provided, looking for offline token')

        try:
            offline_token = os.environ['CYPERF_OFFLINE_TOKEN']
        except KeyError as e:
            parser.error(f'Couldn\'t find environment variable {e}')

    return args, offline_token

    