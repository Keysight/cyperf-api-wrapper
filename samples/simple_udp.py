import time
import cyperf
import utils
from pprint import pprint

class UDPTest (object):
    def __init__ (self, agent_map={}):
        args, offline_token = utils.parse_cli_options ()
        self.utils          = utils.Utils (args.controller,
                                           username=args.user,
                                           password=args.password,
                                           refresh_token=offline_token,
                                           license_server=args.license_server,
                                           license_user=args.license_user,
                                           license_password=args.license_password)

        self.session        = self.utils.create_session_by_config_name ('CyPerf AppMix')
        if not self.session:
            return

        self.agent_map      = agent_map
        self.test_duration  = 60
        self.local_stats    = {}

    def __del__ (self):
        self._release()

    def __enter__ (self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback): 
        self._release()
        if exception_value:
            raise (exception_value)

    def _release (self):
        try:
            if self.session:
                print ('Deleting session')
                self.utils.delete_session (self.session)
                print ('Deleted session')
                self.session = None
        except AttributeError:
            pass

    def _set_objective_and_timeline (self):
        # Change the objective type to 'Simulated Users'. 'Throughput' is not yet supported for UDP Stream.
        self.utils.set_objective_and_timeline (self.session, objective_type=cyperf.ObjectiveType.SIMULATED_USERS, objective_value=1000, test_duration=self.test_duration)

    def configure (self):
        print ('Configuring ...')

        # The order is super important but why????
        self.utils.add_app(self.session, 'UDP Stream')
        self.utils.disable_automatic_network (self.session)
        self.utils.assign_agents (self.session, self.agent_map)
        self._set_objective_and_timeline ()

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

    def _print_run_time_stats (self, test, time_from, time_to):
        stat_names = ['client-streaming-rate', 'server-streaming-rate']
        return self.print_run_time_stats (test, time_from, time_to, stat_names)

    def print_run_time_stats (self, test, time_from, time_to, stat_names):
        last_monitored_time_stamp = None
        for stat_name in stat_names:
            stats = self.utils.collect_stats (test, stat_name, time_from, time_to, self._process_stats)
            if stat_name not in stats:
                continue

            stats           = stats[stat_name]
            last_time_stamp = max(stats)

            if stat_name in self.last_recorded_time_stamps:
                last_recorded_time_stamp = self.last_recorded_time_stamps[stat_name]
            else:
                last_recorded_time_stamp = 0

            if last_time_stamp != last_recorded_time_stamp:
                last_stats      = stats[last_time_stamp]

                print(f'\n{stat_name} at {self.utils.format_milliseconds(last_time_stamp)}\n')
                lines = self.utils.format_stats_dict_as_table(last_stats)
                for line in lines:
                    print (line)

                self.last_recorded_time_stamps[stat_name] = last_time_stamp

            if last_monitored_time_stamp:
                last_monitored_time_stamp = min (max(last_time_stamp, time_from), last_monitored_time_stamp)
            else:
                last_monitored_time_stamp = max(last_time_stamp, time_from)

        return last_monitored_time_stamp

    def _wait_until_stopped (self):
        self.last_recorded_time_stamps = {}
        self.utils.wait_for_test_stop (self.session, self._print_run_time_stats)
        print ('Stopped test ...')

    def run (self):
        self._start ()
        self._wait_until_stopped()

    def collect_final_stats (self):
        print ('Collecting final statistics ...')
        stat_names  = ['client-streaming-statistics', 'server-streaming-statistics']
        session_api = cyperf.SessionsApi(self.utils.api_client)
        test        = session_api.get_test (session_id = self.session.id)
        self.print_run_time_stats (test, 0, -1, stat_names)
        print ('Collected final statistics ...')

if __name__ == '__main__':
    agents = {
        'IP Network 1': ['10.36.75.220'],
        'IP Network 2': ['10.36.75.37']
    }
    with UDPTest (agents) as test:
        test.configure ()
        test.run ()
        test.collect_final_stats ()
