from common.send_method import SendMethod
import requests

SendMethodEntity = SendMethod(requests.session())
SendMethodEntity.login()


