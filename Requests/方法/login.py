import requests
import re

class Blog():
    def __init__(self, s):
        s = requests.session()
        self.s = s

    def login(self):
        url = "http://autoops-auth.q1.com/api/login/ldap"
        header = {
            "x-csrf-token": "x-csrf-token",
            "gameId": 2017,
            "regionId": "TJZYY",
}
        data = {
            "userName": "hecaoyi",
            "password": "Hecaoyi520."
        }
        s = requests.session
        r = requests.post(url, header=header, data=data)
        print(r.json())
