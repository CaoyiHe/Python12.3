# coding=utf-8
from http.cookiejar import CookieJar

import requests
import json

requests.session().get(url)

class Test():
    def __init__(self):
        s = requests.session()
        self.s = s
        self.headers = {}

    def test_login(self):
        url = "http://autoops-auth.q1.com/api/login/ldap"
        # headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {
            'userName': 'hecaoyi',
            'password': 'Hecaoyi520.'
        }
        r = s.post(url=url, json=data)
        print(self.headers)
        print(r.cookies)
        print(r.status_code)

    def test_chaxun(self):
        url = "http://autoops-test.q1.com/api/gameworld/tree?gameId=2117&regionId=TJZYY"
        r1 = s.get(url=url)
        print(r1.json())
        return r1.json()

    def test_chaxun1(self):
        url = "http://autoops-test.q1.com/api/task/create-verify"
        data = {"gameId": 2117, "regionId": "TJZYY", "worldIds": [7779]}
        r2 = s.post(url=url, json=data)
        print(r2.json())
        return r2.json()


if __name__ == "__main__":
    s = requests.session()
    Test = Test()
    Test.test_login()
    Test.test_chaxun()
    Test.test_chaxun1()
