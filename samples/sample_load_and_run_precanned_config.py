import cyperf
from time import sleep
import urllib3; urllib3.disable_warnings()

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cyperf.Configuration(
    host = 'https://10.38.68.208',
    username='admin',
    password='CyPerf&Keysight#1'
)

# Enter a context with an instance of the API client
with cyperf.ApiClient(configuration) as api_client:
    # Find the pre-canned config
    api_config_instance  = cyperf.ConfigurationsApi(api_client)
    take = 1                                                    # int | The number of search results to return (optional)
    skip = None	                                                # int | The number of search results to skip (optional)
    search_col = 'displayName'                                  # str | A list of comma-separated columns used to search for the supplied values (optional)
    search_val = 'Not Working From Home Traffic Mix'            # str | The keywords used to filter the items (optional)
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
        print("Creating session from config called 'Not Working From Home Traffic Mix' ...")
        api_session_response = api_session_instance.create_sessions(session=sessions)
        session = api_session_response[0]
        print("Session created.\n")
    except Exception as e:
        print("Exception when calling SessionsApi->create_sessions: %s\n" % e)

    # Get the configuration of the created session
    include = 'Config, TrafficProfiles'                          # str | Specifies if the sub-fields that are objects should be included (eg. 'Config'). (optional)
    config = api_session_instance.get_config(session_id=session.id, include=include)

    # Modify test duration
    config.config.traffic_profiles[0].objectives_and_timeline.primary_objective.timeline[1].duration = 30
    config.config.traffic_profiles[0].objectives_and_timeline.primary_objective.update()

    # Get available agents
    api_agents_instance = cyperf.AgentsApi(api_client)
    take = None                                                 # int | The number of search results to return (optional)
    skip = None                                                 # int | The number of search results to skip (optional)
    search_col = None                                           # str | A list of comma-separated columns used to search for the supplied values (optional)
    search_val = None                                           # str | The keywords used to filter the items (optional)
    filter_mode = None                                          # str | The operator applied to the supplied values (optional)
    sort = None                                                 # str | A list of comma-separated field:direction pairs used to sort the items where direction must be asc or dsc (optional)
    exclude_offline = 'true'                                    # str | Indicates whether offline agents should be excluded (optional)
    agents = api_agents_instance.get_agents(take=take,
                                            skip=skip,
                                            search_col=search_col,
                                            search_val=search_val,
                                            filter_mode=filter_mode,
                                            sort=sort,
                                            exclude_offline=exclude_offline)

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
    try:
        api_test_operation_response = api_test_operation_instance.start_start_traffic(session_id=session.id)
        api_test_operation_response.await_completion()
    except Exception as e:
        print("Exception when calling TestOperationsApi->start_start_traffic: %s\n" % e)

    # Wait for the test to be finished
    print("Test running ...")
    try:
        api_session_response = api_session_instance.get_test(session.id)
        while(api_session_response.status != 'STOPPED'):
            sleep(5)
            api_session_response = api_session_instance.get_test(session.id)
    except Exception as e:
        print("Exception when calling SessionsApi->get_test: %s\n" % e)
    print("Test finished successfully.\n")

    # Download the test results
    print("Downloading test results ...")
    api_test_results_instance = cyperf.TestResultsApi(api_client)
    generate_all_operation = cyperf.GenerateAllOperation()
    try:
        api_test_results_response = api_test_results_instance.start_results_generate_all(result_id=session.test.test_id, generate_all_operation=generate_all_operation)
        file_path = api_test_results_response.await_completion()

        last_separator_index = file_path.rfind("\\")
        directory = file_path[:last_separator_index]
        file_name = file_path[last_separator_index + 1:]

        print("Saved as: '" + file_name + "' at:\n" + directory)
    except Exception as e:
        print("Exception when calling ReportsApi->start_results_generate_all: %s\n" % e)
