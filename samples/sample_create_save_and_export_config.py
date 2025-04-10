import time

import cyperf
from cyperf import ApplicationProfile, NetworkProfile, IPNetwork, AgentAssignments, ConfigId
from cyperf.utils import create_api_client_cli

if __name__ == "__main__":
    import urllib3; urllib3.disable_warnings()
    
    # Enter a context with an instance of the API client
    with create_api_client_cli(verify_ssl=False) as api_client:
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
        print("Creating empty session...")
        api_session_response = api_session_instance.create_sessions(session=sessions)
        session = api_session_response[0]
        print("Session created.\n")

        # Add an app profile
        session.config.config.traffic_profiles.append(ApplicationProfile(Name="Application Profile"))
        session.config.config.traffic_profiles.update()

        # Get some applications
        api_application_resources_instance = cyperf.ApplicationResourcesApi(api_client)
        take = 4                                                    # int | The number of search results to return (optional)
        skip = 0                                                    # int | The number of search results to skip (optional)
        search_col = 'Name'                                         # str | A list of comma-separated columns used to search for the supplied values (optional)
        search_val = 'Google'                                       # str | The keywords used to filter the items (optional)
        filter_mode = None                                          # str | The operator applied to the supplied values (optional)
        sort = 'Name:asc'                                           # str | A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc (optional)

        application_ids = []
        application_names = []
        print("Finding first 4 applications with 'Google' in their name, sorted alphabetically...")
        api_application_resources_response = api_application_resources_instance.get_resources_apps(take=take, skip=skip, search_col=search_col, search_val=search_val, filter_mode=filter_mode, sort=sort)
        print(f"{len(api_application_resources_response.data)} applications found.\n")
        if len(api_application_resources_response.data) != 4:
            raise ValueError("Couldn't find 4 applications.")
        application_ids = [app.id for app in api_application_resources_response.data]
        application_names = [app.name for app in api_application_resources_response.data]

        # Add the applications
        print("Adding the applications...")
        traffic_profile_id = '1'                                    # str | The ID of the traffic profile.
        external_resource_info = []                                 # List[ExternalResourceInfo] |  (optional)
        for count in range(len(application_ids)):
            temp_external_resource_info = cyperf.ExternalResourceInfo(externalResourceURL=str(application_ids[count]))
            external_resource_info.append(temp_external_resource_info)
            print(f"{application_names[count]} added successfully.")

        api_session_response = api_session_instance.start_config_add_applications(session.id, traffic_profile_id, external_resource_info=external_resource_info)
        api_session_response.await_completion()
        print("Applications added successfully.\n")

        # Create a Network Profile
        print("Adding network elements...")
        network_profile = NetworkProfile(IPNetworkSegment=[], id="1")
        session.config.config.network_profiles.append(network_profile)
        session.config.config.network_profiles.update()

        # Create IP Networks
        client_ip_network = IPNetwork(name="IP Network 1", id="1", agentAssignments=AgentAssignments(by_tag=[]), minAgents=1)
        server_ip_network = IPNetwork(name="IP Network 2", id="2", agentAssignments=AgentAssignments(by_tag=[]), minAgents=1)

        # Append the IP Networks to the Network Profile
        session.config.config.network_profiles[0].ip_network_segment = [client_ip_network, server_ip_network]
        session.config.config.network_profiles[0].ip_network_segment.update()
        print("Client and Server network segments added successfully.\n")

        # Get the configuration of the created session
        include = 'Config, TrafficProfiles'                          # str | Specifies if the sub-fields that are objects should be included (eg. 'Config'). (optional)
        config = api_session_instance.get_session_config(session_id=session.id, include=include)

        # Modify test duration
        config.config.traffic_profiles[0].objectives_and_timeline.primary_objective.timeline[1].duration = 30
        config.config.traffic_profiles[0].objectives_and_timeline.primary_objective.update()

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
        for net_profile in config.config.network_profiles:
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
            time.sleep(5)
            session.refresh()
        print("Test finished successfully.\n")

        # Save the config
        save_config_operation = cyperf.SaveConfigOperation()
        save_config_operation.name = "Sample Script Name"
        saving_response = ''
        print("Saving the configuration...")
        api_save_config_response = api_session_instance.start_session_config_save(session.id, save_config_operation=save_config_operation)
        saving_response = api_save_config_response.await_completion()
        print("Configuration saved successfully.\n")

        # Get configuration's id
        config_id = saving_response["id"]

        # Export the configuration
        api_configurations_instance = cyperf.ConfigurationsApi(api_client)
        export_all_operationn = cyperf.ExportAllOperation(configIds=[ConfigId(id=config_id)])
        api_configurations_response = api_configurations_instance.start_configs_export_all(export_all_operation=export_all_operationn)
        file_path = api_configurations_response.await_completion()
        
        last_separator_index = file_path.rfind("\\")
        directory = file_path[:last_separator_index]
        file_name = file_path[last_separator_index + 1:]
    
        print(f"Exported as: '{file_name}' at {directory}\n")

