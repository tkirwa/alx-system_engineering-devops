#!/usr/bin/env python3

from datadog_api_client import Configuration, ThreadedApiClient
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

configuration = Configuration()

# configuration.api_key["apiKeyAuth"] = "<API KEY>"
configuration.api_key["apiKeyAuth"] = "<API KEY>"

# configuration.api_key["appKeyAuth"] = "<APPLICATION KEY>"
configuration.api_key["appKeyAuth"] = (
    "<APPLICATION KEY>"
)

with ThreadedApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    result = api_instance.list_dashboards()
    dashboards = result.get()
    print(dashboards)
