#!/usr/bin/env python3

from datadog_api_client import Configuration, ThreadedApiClient
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

configuration = Configuration()

# configuration.api_key["apiKeyAuth"] = "<API KEY>"
configuration.api_key["apiKeyAuth"] = "0284acc822e2cae9eb6d87a8feec9728"

# configuration.api_key["appKeyAuth"] = "<APPLICATION KEY>"
configuration.api_key["appKeyAuth"] = (
    "7ace841f3ec33b1d15ef6f03f7c05e339d1d8bfd"
)

with ThreadedApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    result = api_instance.list_dashboards()
    dashboards = result.get()
    print(dashboards)
