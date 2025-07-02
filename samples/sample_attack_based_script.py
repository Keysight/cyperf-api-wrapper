import cyperf
from cyperf import *
from cyperf.utils import create_api_client_cli, TestRunner
from time import sleep
import os 

if __name__ == "__main__":
    import urllib3; urllib3.disable_warnings()
    
    # Enter a context with an instance of the API client
    with create_api_client_cli(verify_ssl=False) as api_client:

        # Get some strikes
        api_application_resources_instance = cyperf.ApplicationResourcesApi(api_client)
        take = 3                                                    # int | The number of search results to return (optional)
        skip = 0                                                    # int | The number of search results to skip (optional)
        search_col = 'Name'                                         # str | A list of comma-separated columns used to search for the supplied values (optional)
        search_val = 'Google Chrome'                         # str | The keywords used to filter the items (optional)
        categories = 'Browser:Chrome'

        strikes = None
        try:
            print(f"Finding first {take} strikes with \'{search_val}\' in their name, from the \'Browser\' category...")
            api_application_resources_response = api_application_resources_instance.get_resources_strikes(take=take, skip=skip, search_col=search_col, search_val=search_val, categories=categories)
            strikes = api_application_resources_response.data
            if len(strikes) != take:
                raise ValueError(f"Couldn't find {take} strikes.")
            
            print(f"{len(strikes)} strikes found:")
            for strike in strikes:
                print(f"    {strike.name}")
            print()

        except Exception as e:
            print("Exception when calling ApplicationResourcesApi->get_resources_strikes: %s\n" % e)


        
        all_files = []
        # Add the attacks
        for strike in strikes:

            # Find the pre-canned empty config
            api_config_instance  = cyperf.ConfigurationsApi(api_client)
            take = 1                                                    # int | The number of search results to return (optional)
            skip = None	                                                # int | The number of search results to skip (optional)
            search_col = 'displayName'                                  # str | A list of comma-separated columns used to search for the supplied values (optional)
            search_val = 'Cyperf Empty Config'                          # str | The keywords used to filter the items (optional)
            filter_mode = None                                          # str | The operator applied to the supplied values (optional)
            sort = None                                                 # str | A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc (optional)
            config = api_config_instance.get_configs(take=1,
                                                    skip=skip,
                                                    search_col=search_col,
                                                    search_val=search_val,
                                                    filter_mode=filter_mode,
                                                    sort=sort)

            if len(config.data) == 0:
                raise ValueError("Couldn't find the specified configuration.")

            # Load a pre-canned config
            api_session_instance = cyperf.SessionsApi(api_client)
            application	= None                                          # str | The user-friendly name for the application that controls this session (optional)
            config_name	= None                                          # str | The display name of the configuration loaded in the session (optional)
            config_url = config.data[0].config_url                      # str | The external URL of the configuration loaded in the session (optional)
            index = None                                                # int | The session's index (optional) (readonly)
            name = None                                                 # str | The user-visible name of the session (optional)
            owner = None                                                # str | The user-visible name of the session's owner (optional) (readonly)
            sessions = [cyperf.Session(application=application,
                                    config_name=config_name,
                                    configUrl=config_url,
                                    index=index,
                                    name=name,
                                    owner=owner)]
            # Create a session
            session = None
            try:
                print("Creating empty session...")
                api_session_response = api_session_instance.create_sessions(sessions=sessions)
                session = api_session_response[0]
                print("Session created.\n")
            except Exception as e:
                print("Exception when calling SessionsApi->create_sessions: %s\n" % e) # Add an app profile        

            # Create an attack profile
            print("Creating a Attack Profile...")
            attack_profile_name = "Custom Attack Profile"
            session.config.config.attack_profiles.append(cyperf.AttackProfile(id="1", name="My Attack Profile", attacks=[]))
            session.config.config.attack_profiles.update()
            print(attack_profile_name + " created succesfully.\n")

            take = 1                                                    # int | The number of search results to return (optional)
            skip = 0                                                    # int | The number of search results to skip (optional)
            search_col = 'Name'                                         # str | A list of comma-separated columns used to search for the supplied values (optional)
            search_val = strike.name                                    # str | The keywords used to filter the items (optional)

            attack = None
            try:
                print(f"Finding the attack with the same name as the strike...")
                api_application_resources_response = api_application_resources_instance.get_resources_attacks(take=take, skip=skip, search_col=search_col, search_val=search_val, categories=categories)
                attack = api_application_resources_response.data[0]
                print("Attack found.")

            except Exception as e:
                print("Exception when calling ApplicationResourcesApi->get_resources_attacks: %s\n" % e)

            session.config.config.attack_profiles[0].attacks.append(Attack(id = "1", name = strike.name, external_resource_url = attack.id))
            session.config.config.attack_profiles[0].attacks.update()
            
        
            print(f"Attack {strike.name} added successfully.\n")

            # Set the objective to single iteration 
            print("Setting the Iteration Count to 1...")
            session.config.config.attack_profiles[0].objectives_and_timeline.timeline_segments[0].iteration_count = 1
            session.config.config.attack_profiles[0].objectives_and_timeline.update()
            print("Iteration Count setted to 1 successfully.\n")

            # Create IP Networks
            client_ip_network = IPNetwork(name="IP Network 1", id="1", agentAssignments=AgentAssignments(by_tag=[]), minAgents=1)
            server_ip_network = IPNetwork(name="IP Network 2", id="2", agentAssignments=AgentAssignments(by_tag=[]), minAgents=1)

            # Append the IP Networks to the Network Profile
            session.config.config.network_profiles[0].ip_network_segment = [client_ip_network, server_ip_network]
            session.config.config.network_profiles[0].ip_network_segment.update()
            print("Client and Server network segments added successfully.\n")

            # Get available agents
            api_agents_instance = cyperf.AgentsApi(api_client)
            agents = api_agents_instance.get_agents(exclude_offline='true')

            if len(agents) < 2:
                raise ValueError("Expected at least 2 active agents")

            # Create an agent map
            agent_map = {
                'IP Network 1': [agents[0].id, agents[0].ip],
                'IP Network 2': [agents[1].id, agents[1].ip]
            }

            # Assign the agents
            print("Assigning agents ...")
            for net_profile in session.config.config.network_profiles:
                for ip_net in net_profile.ip_network_segment:
                    if ip_net.name in agent_map:
                        agent_ip = agent_map[ip_net.name][1]
                        print(f"	Agent {agent_ip} assigned to {ip_net.name}.")
                        capture_settings = None                         # str | The capture settings of the agent that is assigned (optional)
                        interfaces = None                               # List[str] | The names of the assigned test interfaces for the agent (optional)
                        links = None                                    # List[APILink] |  (optional)
                        agent_id = agent_map[ip_net.name][0]
                        agentDetails = [cyperf.AgentAssignmentDetails(agent_id=agent_id,
                                                                    capture_setting=capture_settings,
                                                                    id=agent_id,
                                                                    interfaces=interfaces,
                                                                    links=links)]

                        if not ip_net.agent_assignments:
                            by_id = None                                # List[AgentAssignmentDetails] | The agents statically assigned to the current test configuration (optional)
                            by_port	= None                              # List[AgentAssignmentByPort] | The ports assigned to the current test configuration (optional)
                            by_tag = []                                 # List[str]	| The tags according to which the agents are dynamically assigned
                            links = None                                # List[APILink] |  (optional)
                            ip_net.agent_assignments = cyperf.AgentAssignments(by_id=by_id,
                                                                            by_port=by_port,
                                                                            by_tag=by_tag,
                                                                            links=links)

                        ip_net.agent_assignments.by_id.extend(agentDetails)
                        ip_net.update()
            print("Assigning agents completed.\n")

            # Start traffic
            print("Starting the test ...")
            api_test_operation_instance = cyperf.TestOperationsApi(api_client)
            api_test_operation_response = api_test_operation_instance.start_test_run_start(session_id=session.id)
            api_test_operation_response.await_completion()

            # Wait for the test to be finished
            print("Test running ...")
            session.refresh()
            while session.test.status != 'STOPPED':
                sleep(5)
                session.refresh()
            print("Test finished successfully.\n")

            # Download the test results
            print("Downloading test results ...")
            api_reports_instance = cyperf.ReportsApi(api_client)
            generate_csv_operation = cyperf.GenerateCSVReportsOperation()
            api_test_results_response = api_reports_instance.start_result_generate_csv(result_id=session.test.test_id, generate_csv_reports_operation=generate_csv_operation)
            file_path = api_test_results_response.await_completion()
            
            last_separator_index = file_path.rfind("\\")
            directory = file_path[:last_separator_index]
            file_name = file_path[last_separator_index + 1:]

            print(f"Saved as: '{file_name}' at {directory}\n")

            # Add the file path to the list
            all_files.append(file_path)
        
        
        print("Aggregating all CSV files ...")
        aggregated_file_path = os.path.join(directory, "aggregated_all_strikes_attack.csv")

        with open(aggregated_file_path, 'w', encoding='ISO-8859-1') as outfile:
            for i, file_path in enumerate(all_files):
                with open(file_path, 'r', encoding='ISO-8859-1') as infile:
                    if i == 0:
                        outfile.write(infile.read())
                    else:
                        next(infile)
                        outfile.write(infile.read())

        print(f"Aggregated results saved as: '{aggregated_file_path}'")


