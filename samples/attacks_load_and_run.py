import os
import time
import cyperf
import utils
from pprint import pprint

class AttackTest(object):
    def __init__ (self, agent_map={}):
        config_file         = './cyperf-configurations/Cyperf-Attacks-Test.zip'

        args, offline_token = utils.parse_cli_options ()
        self.utils          = utils.Utils (args.controller,
                                           username=args.user,
                                           password=args.password,
                                           refresh_token=offline_token,
                                           license_server=args.license_server,
                                           license_user=args.license_user,
                                           license_password=args.license_password)

        self.config         = self.utils.load_configuration_file(config_file)
        _, config_url       = self.config
        self.session        = self.utils.create_session(config_url)

        self.agent_map      = agent_map
        self.local_stats    = {}

    def __del__ (self):
        self._release()

    def __enter__ (self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback): 
        self._release()
        if exception_value:
            raise (exception_value)

    def _release(self):
        try:
            if self.session:
                self.utils.delete_session (self.session)
                self.session = None
        except AttributeError:
            pass

        try:
            if self.config:
                config_id, _ = self.config
                self.utils.remove_configuration(config_id)
                self.config  = None
        except AttributeError:
            pass

    def configure(self):
        print ('Configuring ...')
        self.utils.assign_agents (self.session, self.agent_map)
        print ('Configured ...')

    def _start (self):
        print ('Starting test ...')
        self.utils.start_test (self.session)
        print ('Started test ...')

    def _process_stats (self, stats):
        processed_stats = self.local_stats
        for stat in stats:
            if stat.snapshots:
                processed_stats [stat.name] = {}
                for snapshot in stat.snapshots:
                    time_stamp = snapshot.timestamp
                    processed_stats [stat.name][time_stamp] = []
                    d = {}
                    for idx, stat_name in enumerate(stat.columns):
                        d [stat_name] = [val[idx].actual_instance for val in snapshot.values]
                    processed_stats [stat.name][time_stamp] = d
        return processed_stats

    def _print_attack_stats (self, test, time_from, time_to):
        stat_name    = 'all-strikes-attack'
        attack_stats = self.utils.collect_stats (test, stat_name, time_from, time_to, self._process_stats)
        if stat_name not in attack_stats:
            return None

        attack_stats    = attack_stats[stat_name]
        last_time_stamp = max(attack_stats)
        if last_time_stamp != self.last_recorded_time_stamp:
            last_stats      = attack_stats[last_time_stamp]

            print(f'\n{stat_name} at {self.utils.format_milliseconds(last_time_stamp)}\n')
            lines = self.utils.format_stats_dict_as_table(last_stats)
            for line in lines:
                print (line)

            self.last_recorded_time_stamp = last_time_stamp
        return max(last_time_stamp, time_from)

    def _wait_until_stopped (self):
        self.last_recorded_time_stamp = 0
        self.utils.wait_for_test_stop (self.session, self._print_attack_stats)
        print ('Stopped test ...')

    def run(self):
        self._start ()
        self._wait_until_stopped()

    def collect_final_stats(self):
        # Run time stats may be sufficient.
        # Please add here if some other stats should be checked at the end.
        pass

if __name__ == '__main__':
    agents = {
        'PAN-FW-Client': ['10.36.75.220'],
        'AWS-NW-FW-Client': ['10.36.75.66'],
        'PAN-FW-Server': ['10.36.75.37'],
        'AWS-NW-FW-Server': ['10.36.75.65']
    }
    with AttackTest (agents) as test:
        test.configure ()
        test.run ()
        test.collect_final_stats ()
