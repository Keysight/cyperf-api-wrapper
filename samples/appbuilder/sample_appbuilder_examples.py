import cyperf, random, string
from cyperf import CreateAppOperation, ParameterMeta, ParameterMatch, RegexMatch, ActionInput, CaptureInput, \
    AppFlowInput
from cyperf.utils import parse_cli_options


def _create_api_client_from_cli():
    args, offline_token = parse_cli_options()

    configuration = cyperf.Configuration(
        host=f"https://{args.controller}",
        refresh_token=offline_token,
        username=args.user,
        password=args.password,
    )
    configuration.verify_ssl = False
    api_client = cyperf.ApiClient(configuration)

    return api_client

def random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def get_capture_id(capture_upload_result):
    return capture_upload_result['resourceURL'].split('/')[-1]

def app_params(param_name: str, patterns: list[str], match_location: list[str]):
    regex_match = RegexMatch(
        Patterns=patterns
    )
    param_match = ParameterMatch(
        MatchLocation=match_location, # URL, REQ_HEADERS, RES_HEADERS, REQ_BODY, RES_BODY
        MatchType="REGEX",
        RegexMatch=regex_match
    )
    param_anthropic_version = ParameterMeta(
        Name=param_name,
        Matches=[param_match]
    )
    return [param_anthropic_version]

def action_get_models(capture_id):
    get_models_flow = AppFlowInput(
        AppFlowId="2",
        Exchanges=["1"]
    )
    get_models_content = CaptureInput(
        CaptureId=capture_id,
        Flows=[get_models_flow]
    )
    return ActionInput(
        Name="Get Models",
        Captures=[get_models_content],
        Parameters=app_params("Claude Model", ["claude-opus-4-6|claude-sonnet-5"], ["REQ_BODY", "RES_BODY"])
    )

def action_ask_claude(capture_id):
    get_models_flow = AppFlowInput(
        AppFlowId="2",
        Exchanges=["2"]
    )
    get_models_content = CaptureInput(
        CaptureId=capture_id,
        Flows=[get_models_flow]
    )
    return ActionInput(
        Name="Ask Claude",
        Captures=[get_models_content],
        Parameters=app_params("Claude Model", ["claude-opus-4-6|claude-sonnet-5"], ["REQ_BODY", "RES_BODY"])
    )

def actions(capture_id):
    return [action_get_models(capture_id), action_ask_claude(capture_id)]

def new_action(action_name: str, capture_id: str, flow_id: str, exchanges: list[str]):
    return ActionInput(
        Name=action_name,
        Captures=[CaptureInput(
            CaptureId=capture_id,
            Flows=[AppFlowInput(
                AppFlowId=flow_id,
                Exchanges=exchanges
            )]
        )]
    )

def one_action_per_exchange(client, capture_id):
    flows = client.get_capture_flows(capture_id=capture_id)
    actions = []
    for flow in flows:
        exchanges = client.get_flow_exchanges(capture_id=capture_id, flow_id=flow.id)
        for exchange in exchanges:
            actions.append(new_action(exchange.name, capture_id, flow.id, [exchange.id]))

    return actions

def one_action_all_exchanges(client, action_name, capture_id):
    flows = client.get_capture_flows(capture_id=capture_id)
    actions = []
    for flow in flows:
        actions.append(new_action(action_name, capture_id, flow.id, ["all"]))

    return actions


def create_claude_app(client):
    new_claude_app = CreateAppOperation(
        AppName=f"Anthropic Claude ({random_string(8)})",
        Description="This is a dummy implementation of Anthropic Claude Application",
        Actions=actions(capture_id),
        Parameters=app_params("Anthropic Version", ["Anthropic-Version.*"], ["REQ_HEADERS"])
    )

    create_app_op = client.start_resources_create_app(new_claude_app)
    create_app_op.await_completion()

def create_app_with_one_action_for_each_exch(client, capture_id):
    new_action_per_exch_app = CreateAppOperation(
        AppName=f"Generic app ({random_string(8)})",
        Description="This is a sample application generated from a capture, there is one action for each exchange in the original capture",
        Actions=one_action_per_exchange(client, capture_id),
    )

    create_app_op = client.start_resources_create_app(new_action_per_exch_app)
    create_app_op.await_completion()

def create_app_with_one_action_all_exchanges(client, capture_id):
    new_action_per_exch_app = CreateAppOperation(
        AppName=f"Generic app ({random_string(8)})",
        Description="This is a sample application generated from a capture, there is one action for each exchange in the original capture",
        Actions=one_action_all_exchanges(client, "Generic Action", capture_id),
    )

    create_app_op = client.start_resources_create_app(new_action_per_exch_app)
    create_app_op.await_completion()


if __name__ == "__main__":
    import urllib3

    urllib3.disable_warnings()

    api_client = _create_api_client_from_cli()

    with api_client:
        resource_api = cyperf.ApplicationResourcesApi(api_client)
        upload_op = resource_api.start_resources_captures_encrypted_upload_file(file="claude.pcap", ssl_key_log_file="tls_key.log")

        #use this method instead if the capture is not encrypted or you do not have the decryption keys(TCP flows will be parsed instead)
        #upload_op = resource_api.start_resources_captures_upload_file(file="claude.pcap")

        capture_upload_result = upload_op.await_completion()
        capture_id = get_capture_id(capture_upload_result)

        # creates one application, starting from the uploaded capture, creates a single action with all the exchanges from all the flows
        create_app_with_one_action_all_exchanges(resource_api, capture_id)

        # creates one application, starting from the uploaded capture, creates a single action for each exchange in each flow
        create_app_with_one_action_for_each_exch(resource_api, capture_id)

        # creates one application with some specific logic(choose specific exchanges from specific flows) and add parameters to the application
        create_claude_app(resource_api)
