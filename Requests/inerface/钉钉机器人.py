import requests
from common.session import SendMethodEntity
from common.send_method import SendMethod

class DingDing:
    def __init__(self):
        self.url = "https://oapi.dingtalk.com/robot/send?access_token=7fb367800c0cb2e95d6140cba391d449c8b2b98185b02151fa0af00a9508015e"
        self.method = "post"
        self.headers = {"Content-Type": "application/json"}

    def ding(self):
        data = {
            "msgtype": "text",
            "text": {
                "content": "test:test"
            }
        }
        response = SendMethodEntity.send_method(self.method, self.url, headers=self.headers, data=data)
        print(response)


if __name__ == '__main__':
    print("hallo")
    print(DingDing().ding())
