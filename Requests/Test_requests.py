import requests
import json


def test_get():
    open_api_url_prefix = "https://ad.oceanengine.com/open_api/"
    uri = "2/advertiser/fund/daily_stat/"
    url = open_api_url_prefix + uri
    params = {
        "advertiser_id": 1649891404707854,
        "start_date": "2018-01-01",
        "end_date": "2021-01-12"
    }
    headers = {"Access-Token": "9ddeb583f72ac6b4e18a743e351f28e1e43fc309"}
    r = requests.get(url=url, json=params, headers=headers)
    print(r.json())


test_get()
