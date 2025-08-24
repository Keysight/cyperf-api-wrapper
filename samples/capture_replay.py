import cyperf
import os
import re
import utils
import urllib3; urllib3.disable_warnings()
import argparse
import yaml 
from pprint import pprint
import asyncio
import csv
import pandas as pd
from collections import Counter

file_path = '/mnt/c/new_python_automation_panw/cyperf-api-wrapper/samples/test_parameters.yml'

def remove_suffix(string, suffix="-base"):
    if string.endswith(suffix):
        return string[:-len(suffix)]
    return string

def find_indices(my_list, target_string, exact_match):
    if exact_match:
        return [i for i, s in enumerate(my_list) if s == target_string]
    else:
        return [i for i, s in enumerate(my_list) if target_string in s]

def select_best_matching_app(dump_app_list,cyperf_apps):
    #print(dump_app_list)
    # Count the frequency of each string
    freq = Counter(dump_app_list)
    #check for the highest freuency 
    sorted_list = sorted(dump_app_list, key=lambda x: freq[x], reverse=True)
    return sorted_list
    



def convert_app_names_to_common_names(application_dict):
    for item in application_dict:
        app_name= item
        #if the user-specified application name does not contain hyphen('-') then include it as-is in the list
        if(app_name.find("-")==-1):
            application_dict[item].append(app_name)
        #if the user-specified application name contains suffix ( -base ) , prefix (ms-) ,etc  remove them . This will help in search.
        else:
            temp_list= re.split(r"[- ]", app_name)
            # This needs to be updated on regular basis 
            strings_to_remove=["base","ms","as","ds"]
            result = [s for s in temp_list if s not in strings_to_remove]
            application_dict[item].extend(result)
    return application_dict


#read a yml file and return a dictionary 
def read_yaml_file(file_path):
  
    try:
        with open(file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
            return yaml_data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return {}

#read the test_parameters from the yml file and populate into variables 
yaml_dict = read_yaml_file(file_path)

print(yaml_dict)

#populate the variables with user inputs
capture_folder_path                   = yaml_dict["location_of_folder_containing_captures"]
name_of_existing_cyperf_configuration = yaml_dict["name_of_existing_cyperf_configuration"]
csv_path                              = yaml_dict["csv_path"]
exact_match                           = yaml_dict["exact_match"]

#Load the configuration or check if the configuration is already loaded and having an active session id.
class AppMixBuilderTest (object):
    def __init__ (self, capture_folder_path ,name_of_existing_cyperf_configuration ,csv_path , agent_map={}):
        args, offline_token = utils.parse_cli_options()
        self.utils          = utils.Utils(args.controller,
                                          username=args.user,
                                          password=args.password,
                                          refresh_token=offline_token,
                                          license_server=args.license_server,
                                          license_user=args.license_user,
                                          license_password=args.license_password)



        self.capture_folder_path                      = capture_folder_path
        self.name_of_existing_cyperf_configuration    = name_of_existing_cyperf_configuration
        self.csv_path                                 = csv_path
        self.agent_map                                = agent_map
        self.local_stats                              = {}

    def __del__(self):
        self._release()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback): 
        self._release()
        if exception_value:
            raise (exception_value)

    def _release(self):
        try:
            if self.session:
                print('Deleting session')
                self.utils.delete_session(self.session)
                print('Deleted session')
                self.session = None
        except AttributeError:
            pass

    def _set_objective_and_timeline(self):
        # Change the objective type to 'Simulated Users'. 'Throughput' is not yet supported for UDP Stream.
        self.utils.set_objective_and_timeline(self.session,
                                              objective_type=cyperf.ObjectiveType.SIMULATED_USERS,
                                              objective_value=1000,
                                              test_duration=self.test_duration)
##SOUMO -- 
    #function to read the input CSV file which contains 2 coulums - (a)Application Name (b) percentage
    def read_csv_file(self):
        data_dict = {}
        with open(self.csv_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    key, value = row
                    data_dict[key] = value
                else:
                    print(f"Skipping row: {row}. Expected 2 columns, but got {len(row)}.")
        return data_dict
    
    def sum_percentage_and_populate_applications(self):
        try:
            df = pd.read_csv(self.csv_path)
            total_percentage = df['percentage'].sum()
            applications = df['application'].tolist()
            percentages = df['percentage'].tolist()
            return total_percentage, applications,percentages
        except pd.errors.EmptyDataError:
            print("The CSV file is empty.")
            return None, None
        except KeyError as e:
            print(f"The CSV file is missing the column: {e}")
            return None, None
    
    def percentages_to_weights(self, percentages):
        total_percentage = sum(percentages)
        weights = [round(p / total_percentage * 100) for p in percentages]
        # Ensure no weight is zero
        min_weight = min(weights)
        if min_weight == 0:
            zero_indices = [i for i, w in enumerate(weights) if w == 0]
            for i in zero_indices:
                weights[i] = 1
            # Adjust weights to ensure they sum up to 100
            diff = sum(weights) - 100
            weights[weights.index(max(weights))] -= diff
        else:
            # Adjust weights to ensure they sum up to 100
            diff = 100 - sum(weights)
            weights[weights.index(max(weights))] += diff
        return weights
                
    def configure_test(self):
        total_percentage, applications, percenatges  = self.sum_percentage_and_populate_applications()
        
        if(total_percentage < 99 or total_percentage > 101):
            print("You must fix the percentages such that they add upto 100 ")
        else:
            weights = self.percentages_to_weights(percenatges)

        input_app_dict = dict(zip(applications, weights)) 
        
        #Search a  configuation by name as provided in the test-aparmeters.yml file ( example - PANW-APPMIX)
        if (self.utils.search_configuration_file(name_of_existing_cyperf_configuration)):
            #load the configuration and create a test session 
            try:
               session_appmix=self.utils.create_session_by_config_name(name_of_existing_cyperf_configuration)
               print("The configuration was loaded successfully !")
            except Exception:
                print("The configuration was not loaded successfully !")
                return False
            
            session_id = session_appmix.id
            #print(session_id)
            
            #check if the apps are present pre-canned in CyPerf 
            app_list = applications

            
            
            #convert this list to a dictionary where the keys are the app names read from the csv supplied by customer and values are list of 
            #names derived from them ( split into tokens , that enables better search ) 
            #For example if the customer provides  a list contains application name as ms-office-base 
            #then we will store it in a dictionary where the key will be 'ms-office-base' and value will be [office].
            # This will enable more hits in the search against CyPerf applications ( pre-canned + custom )

            #create the data-structure as described above
            app_dict={} 
            for index in range(len(applications)):
                app_dict.update({applications[index]:[]})
            
            #The app_dict created above must have weight as the first element in the list 
            #for example if ms-office-base has weight 3
            #The app_dict must have a element ms-office-base as key & [3,"office"] as value 
             
            for item in app_dict:
                weight = input_app_dict[item]
                app_dict[item].append(weight)
            
            #convert the application names mentioned in csv to common names 
            new_app_dict=convert_app_names_to_common_names(app_dict)
            #pprint(new_app_dict)
            #found 
            found=0
            # create a variable called target appmix which we will eventually use for appmix creatin in cyperf Traffic profile 
            target_app_mix_dict={}
            
            #search the application in CyPerf library ( Pre-canned + custom )
            #collect all the applciation from CyPerf Library into a variable 
            cyperf_apps=self.utils.get_apps(session_appmix)
            
            #convert cyPerf app-names them in lower case 
            for i, x in enumerate(cyperf_apps):
                if isinstance(x, str):
                    cyperf_apps[i] = x.lower()
            
            for item in new_app_dict:
                app_list=new_app_dict[item]
                dump_app_list=[]
                for ele in app_list[1:]:
                        indices = find_indices(cyperf_apps,ele,False)
                        if ( len(indices)):
                           temp_list = [cyperf_apps[i] for i in indices]
                           dump_app_list.extend(temp_list)
                        
                #pprint(select_best_matching_app(dump_app_list,cyperf_apps))
                if((select_best_matching_app(dump_app_list,cyperf_apps))):
                    best=select_best_matching_app(dump_app_list,cyperf_apps)[0]
                    weight=new_app_dict[item][0]
                    target_app_mix_dict.update({best:weight})
                    
            #Now you need to tag the weight with this app 
            print(" Target appmix is = ")
            pprint(target_app_mix_dict)

            #coverage percenatge 
            coverage_percent = (len(target_app_mix_dict.keys())/len((new_app_dict.keys())))*100
            print(f"coverage Percentage = {coverage_percent}")

            #add_applications
            self.utils.add_apps_with_weights1(session_appmix,target_app_mix_dict)
            #self.utils.check_if_traffic_enabled(session)
            print ("done!")
            




class CaptureReplayTest (object):
    def __init__(self, capture_folder_path ,agent_map={}):
        args, offline_token = utils.parse_cli_options()
        self.utils          = utils.Utils(args.controller,
                                          username=args.user,
                                          password=args.password,
                                          refresh_token=offline_token,
                                          license_server=args.license_server,
                                          license_user=args.license_user,
                                          license_password=args.license_password)

        
        
        self.capture_folder_path = capture_folder_path
        self.agent_map      = agent_map
        self.test_duration  = 60
        self.local_stats    = {}

    def __del__(self):
        self._release()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback): 
        self._release()
        if exception_value:
            raise (exception_value)

    def _release(self):
        try:
            if self.session:
                print('Deleting session')
                self.utils.delete_session(self.session)
                print('Deleted session')
                self.session = None
        except AttributeError:
            pass

    def _set_objective_and_timeline(self):
        # Change the objective type to 'Simulated Users'. 'Throughput' is not yet supported for UDP Stream.
        self.utils.set_objective_and_timeline(self.session,
                                              objective_type=cyperf.ObjectiveType.SIMULATED_USERS,
                                              objective_value=1000,
                                              test_duration=self.test_duration)
    #soumo
    def get_capture_file_paths(self):
        try:
          # Check if the folder exists
          if not os.path.exists(self.capture_folder_path):
            print(f"Error: Folder '{self.capture_folder_path}' does not exist.")
            return []

          # Get a list of all files in the folder
          file_paths = [os.path.join(self.capture_folder_path, file) for file in os.listdir(self.capture_folder_path) if os.path.isfile(os.path.join(self.capture_folder_path, file))]

          return file_paths

        except Exception as e:
          print(f"An error occurred: {str(e)}")
          return []

    


    async def configure(self):
        print('Configuring ...')
        #read the pcap files 
        list_of_paths_of_pcap_files = self.get_capture_file_paths()
        list_of_paths_of_pcap_files.reverse()
        print(list_of_paths_of_pcap_files)
        #upload all the captures from the specified folder ( in yml file )
        #to CyPerf Resource Library for Captures 
        while(list_of_paths_of_pcap_files):
          capture_file=list_of_paths_of_pcap_files.pop()
          print("uploading capture - {} ".format(capture_file))
          await self.utils.upload_the_capture_file(capture_file)
        #create an application from the uploaded captures 
        apps_created= self.utils.create_apps_from_captures()
        print('Configuration complete !!!.You may now use the custom apps created from pcaps.\nThe custom apps are available under the Resource Library in CyPerf Controller')

    def _start(self):
        print('Starting test ...')
        self.utils.start_test(self.session)
        print('Started test ...')

    def _process_stats(self, stats):
        processed_stats = self.local_stats
        for stat in stats:
            if stat.snapshots:
                processed_stats[stat.name] = {}
                for snapshot in stat.snapshots:
                    time_stamp = snapshot.timestamp
                    processed_stats[stat.name][time_stamp] = []
                    d = {}
                    for idx, stat_name in enumerate(stat.columns):
                        d[stat_name] = [val[idx].actual_instance for val in snapshot.values]
                    processed_stats[stat.name][time_stamp] = d
        return processed_stats

    def _print_run_time_stats(self, test, time_from, time_to):
        stat_names = ['client-streaming-rate', 'server-streaming-rate']
        return self.print_run_time_stats(test, time_from, time_to, stat_names)

    def print_run_time_stats(self, test, time_from, time_to, stat_names):
        last_monitored_time_stamp = None
        for stat_name in stat_names:
            stats = self.utils.collect_stats(test,
                                             stat_name,
                                             time_from,
                                             time_to,
                                             self._process_stats)
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
                    print(line)

                self.last_recorded_time_stamps[stat_name] = last_time_stamp

            if last_monitored_time_stamp:
                last_monitored_time_stamp = min (max(last_time_stamp, time_from),
                                                 last_monitored_time_stamp)
            else:
                last_monitored_time_stamp = max(last_time_stamp, time_from)

        return last_monitored_time_stamp

    def _wait_until_stopped(self):
        self.last_recorded_time_stamps = {}
        self.utils.wait_for_test_stop(self.session, self._print_run_time_stats)
        print('Stopped test ...')

    def run(self):
        self._start()
        self._wait_until_stopped()

    def collect_final_stats(self):
        print('Collecting final statistics ...')
        stat_names  = ['client-streaming-statistics', 'server-streaming-statistics']
        session_api = cyperf.SessionsApi(self.utils.api_client)
        test        = session_api.get_test(session_id=self.session.id)
        self.print_run_time_stats(test, 0, -1, stat_names)
        print('Collected final statistics ...')


def start_test():
      
    agents = {
        'IP Network 1': ['10.39.68.164'],
        'IP Network 2': ['10.39.68.184']
    }
    with AppMixBuilderTest( capture_folder_path,name_of_existing_cyperf_configuration,csv_path,agents) as test1:
        test1.configure_test()
        #test.configure()
        #test.run()
        #test.collect_final_stats()

    '''with CaptureReplayTest(capture_folder_path,agents) as test:
        await test.configure()
        #test.configure()
        #test.run()
        #test.collect_final_stats()'''
    

async def main():
      
    agents = {
        'IP Network 1': ['10.39.68.164'],
        'IP Network 2': ['10.39.68.184']
    }
    
    with CaptureReplayTest(capture_folder_path,agents) as test:
        await test.configure()
        #test.configure()
        #test.run()
        #test.collect_final_stats()

if __name__ == '__main__':
    #asyncio.run(main())
    start_test()
