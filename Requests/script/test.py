from common.session import SendMethodEntity
from inerface.login import Get
from common.send_method import SendMethod


class Tsetget:
    def __init__(self):
        self.get = Get()
        self.SendMethod = SendMethodEntity

    def test_get(self):
        data = {"gameId": 2117, "regionId": "TJZYY", "worldIds": [7779]}
        response = self.get.chaxun(data)
        print(SendMethod.format_response(response))


if __name__ == '__main__':
    Tsetget().test_get()
