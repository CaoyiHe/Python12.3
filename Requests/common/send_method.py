"""
封装请求方式
"""
import requests
import json


class SendMethod:
    session = None

    def __init__(self, session):
        self.session = session

    def send_method(self, method, url, params=None, data=None, headers=None):
        """封装请求方式"""

        if method == "get" or method == "delete":
            response = self.session.request(method=method, url=url, params=params, headers=headers)
        elif method == "post" or method == "put":
            response = self.session.request(method=method, url=url, json=data, headers=headers)
        else:
            print("请求方式不正确")
            response = None
        if method == "delete":
            return response.status_code
        else:
            try:
                return response.json()
            except:
                return response.status_code

    @staticmethod
    def format_response(response):
        """格式化返回数据"""
        return json.dumps(response, indent=2, ensure_ascii=False)

    def login(self):
        url = "http://autoops-auth.q1.com/api/login/ldap"
        data = {
            'userName': 'hecaoyi',
            'password': 'Hecaoyi520.'
        }
        s = self.session.post(url=url, json=data)
        return s
