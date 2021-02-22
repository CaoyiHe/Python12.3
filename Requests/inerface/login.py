from common.session import SendMethodEntity


class Login:

    def __init__(self):
        self.url = "http://autoops-auth.q1.com/api/login/ldap"
        self.method = "post"

    def login(self, data):
        response = SendMethodEntity.send_method(self.method, self.url, data=data)
        return response


class Get:
    def __init__(self, ):
        self.url = "http://autoops-test.q1.com/api/task/create-verify"
        self.method = "post"

    def chaxun(self, data):
        response = SendMethodEntity.send_method(self.method, self.url, data=data)
        return response
