# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Contact: support@keysight.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from cyperf.models.authenticate200_response import Authenticate200Response

from cyperf import DynamicModel
from cyperf.api_client import ApiClient, RequestSerialized
from cyperf.api_response import ApiResponse
from cyperf.rest import RESTResponseType


class AuthorizationApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def authenticate(
        self,
        client_id: Optional[StrictStr] = None,
        grant_type: Annotated[Optional[StrictStr], Field(description="Controls the type of credentials to be used for authentication.")] = None,
        password: Annotated[Optional[StrictStr], Field(description="(only for grant_type: password) The password to use.")] = None,
        refresh_token: Annotated[Optional[StrictStr], Field(description="(only for grant_type: refresh_token) The refresh token. You can obtain this from Gear Menu > Administration > Offline Tokens.")] = None,
        scope: Optional[StrictStr] = None,
        username: Annotated[Optional[StrictStr], Field(description="(only for grant_type: password) The username to use.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Authenticate200Response:
        """authenticate

        Get an access_token and refresh_token with a username+password, or use a refresh_token to generate a new access_token. You can also get a refresh_token from the UI, from Gear Menu > Administration > Offline Tokens. The access_token should be supplied in the Authorization header for all API requests.

        :param client_id:
        :type client_id: str
        :param grant_type: Controls the type of credentials to be used for authentication.
        :type grant_type: str
        :param password: (only for grant_type: password) The password to use.
        :type password: str
        :param refresh_token: (only for grant_type: refresh_token) The refresh token. You can obtain this from Gear Menu > Administration > Offline Tokens.
        :type refresh_token: str
        :param scope:
        :type scope: str
        :param username: (only for grant_type: password) The username to use.
        :type username: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._authenticate_serialize(
            client_id=client_id,
            grant_type=grant_type,
            password=password,
            refresh_token=refresh_token,
            scope=scope,
            username=username,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Authenticate200Response",
        }
        return self.api_client.call_api(
            *_param,
            _response_types_map=_response_types_map,
            _request_timeout=_request_timeout
        )


    @validate_call
    def authenticate_with_http_info(
        self,
        client_id: Optional[StrictStr] = None,
        grant_type: Annotated[Optional[StrictStr], Field(description="Controls the type of credentials to be used for authentication.")] = None,
        password: Annotated[Optional[StrictStr], Field(description="(only for grant_type: password) The password to use.")] = None,
        refresh_token: Annotated[Optional[StrictStr], Field(description="(only for grant_type: refresh_token) The refresh token. You can obtain this from Gear Menu > Administration > Offline Tokens.")] = None,
        scope: Optional[StrictStr] = None,
        username: Annotated[Optional[StrictStr], Field(description="(only for grant_type: password) The username to use.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Authenticate200Response]:
        """authenticate

        Get an access_token and refresh_token with a username+password, or use a refresh_token to generate a new access_token. You can also get a refresh_token from the UI, from Gear Menu > Administration > Offline Tokens. The access_token should be supplied in the Authorization header for all API requests.

        :param client_id:
        :type client_id: str
        :param grant_type: Controls the type of credentials to be used for authentication.
        :type grant_type: str
        :param password: (only for grant_type: password) The password to use.
        :type password: str
        :param refresh_token: (only for grant_type: refresh_token) The refresh token. You can obtain this from Gear Menu > Administration > Offline Tokens.
        :type refresh_token: str
        :param scope:
        :type scope: str
        :param username: (only for grant_type: password) The username to use.
        :type username: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._authenticate_serialize(
            client_id=client_id,
            grant_type=grant_type,
            password=password,
            refresh_token=refresh_token,
            scope=scope,
            username=username,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Authenticate200Response",
        }
        return self.api_client.call_api(
            *_param,
            _response_types_map=_response_types_map,
            _request_timeout=_request_timeout
        )


    @validate_call
    def authenticate_without_preload_content(
        self,
        client_id: Optional[StrictStr] = None,
        grant_type: Annotated[Optional[StrictStr], Field(description="Controls the type of credentials to be used for authentication.")] = None,
        password: Annotated[Optional[StrictStr], Field(description="(only for grant_type: password) The password to use.")] = None,
        refresh_token: Annotated[Optional[StrictStr], Field(description="(only for grant_type: refresh_token) The refresh token. You can obtain this from Gear Menu > Administration > Offline Tokens.")] = None,
        scope: Optional[StrictStr] = None,
        username: Annotated[Optional[StrictStr], Field(description="(only for grant_type: password) The username to use.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """authenticate

        Get an access_token and refresh_token with a username+password, or use a refresh_token to generate a new access_token. You can also get a refresh_token from the UI, from Gear Menu > Administration > Offline Tokens. The access_token should be supplied in the Authorization header for all API requests.

        :param client_id:
        :type client_id: str
        :param grant_type: Controls the type of credentials to be used for authentication.
        :type grant_type: str
        :param password: (only for grant_type: password) The password to use.
        :type password: str
        :param refresh_token: (only for grant_type: refresh_token) The refresh token. You can obtain this from Gear Menu > Administration > Offline Tokens.
        :type refresh_token: str
        :param scope:
        :type scope: str
        :param username: (only for grant_type: password) The username to use.
        :type username: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._authenticate_serialize(
            client_id=client_id,
            grant_type=grant_type,
            password=password,
            refresh_token=refresh_token,
            scope=scope,
            username=username,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Authenticate200Response",
        }
        return self.api_client.call_api(
            *_param,
            _response_types_map=None,
            _request_timeout=_request_timeout
        )


    def _authenticate_serialize(
        self,
        client_id,
        grant_type,
        password,
        refresh_token,
        scope,
        username,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        if client_id is not None:
            _form_params.append(('client_id', client_id))
        if grant_type is not None:
            _form_params.append(('grant_type', grant_type))
        if password is not None:
            _form_params.append(('password', password))
        if refresh_token is not None:
            _form_params.append(('refresh_token', refresh_token))
        if scope is not None:
            _form_params.append(('scope', scope))
        if username is not None:
            _form_params.append(('username', username))
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/x-www-form-urlencoded'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'OAuth2', 
            'OAuth2'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/auth/realms/keysight/protocol/openid-connect/token',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


