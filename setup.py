# coding: utf-8

"""
    CyPerf Application API

    CyPerf REST API

    The version of the OpenAPI document: 1.0.0
    Contact: support@keysight.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "cyperf"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.11"
REQUIRES = [
    "urllib3 >= 2.0.0, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="CyPerf REST API",
    author="Keysight CyPerf",
    author_email="support@keysight.com",
    url="",
    keywords=["cyperf", "keysight"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
CyPerf REST API
===============

This package is a client API for the Keysight CyPerf Controller.

This is a full implementation of all features supported by CyPerf.

# Getting started

To connect to a controller running at https://my-controller, just run the following:

    import cyperf

    config = cyperf.Configuration(host="https://my-controller",
                                  user="admin",
                                  refresh_token="get a token from CyPerf UI > Gear > Offline Token")
    # if you don't have a valid HTTPS certificate for controller, uncomment this line
    # config.verify_ssl = False

    client = cyperf.ApiClient(config)

    sessions_api = cyperf.SessionsApi(client)

    sessions = sessions_api.get_sessions()

    sessions[0].config.config.traffic_profiles[0].name = "My API Traffic Profile"

# Integrating in a regression

This package also includes a `cyperf.utils` component that can be used for easily writing scripts
that can be run from a console and receive credentials through environment variables.

Say `sample.py` contains this code:

    import cyperf

    client = cyperf.utils.create_api_client_cli(verify_ssl=False)

    sessions_api = cyperf.SessionsApi(client)

    sessions = sessions_api.get_sessions()

    sessions[0].config.config.traffic_profiles[0].name = "My API Traffic Profile"

You can then simply run this script like:

    export CYPERF_OFFLINE_TOKEN="get a token from CyPerf UI > Gear > Offline Token"
    python sample.py --controller my-controller --user admin
    
    """,  # noqa: E501
    package_data={"cyperf": ["py.typed"]},
    license='MIT License (MIT) ',
)
