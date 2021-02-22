# coding=utf-8
import requests
import re


class Test_Blog():
    def __init__(self, s):
        s = requests.session
        self.s = s
        self.current_group_id = ''

    def test_login(self):
        url = 'http://59.110.63.111:3000/api/user/login'
        data = {
            "email": "admin@admin.com",
            "password": "ymfe.org"
        }
        # s = requests.session()
        r = s.post(url, data=data)
        # print(r.json()['data']["list"][0]['username'])     正则方法，[第几层][要匹配的字段名]
        # z = (r.json()['data']['username'])
        print(s)
        return r.content.decode('utf-8')

    # def get_postid(self, r):
    #     postid = re.findall(r'"username":"(.+?)"', r)
    #     print(postid)
    #     print(r)
    def test_chuangjian(self):
        url = "http://59.110.63.111:3000/api/project/add"
        data = {
            "name": "test_4",
            "group_id": "14",
            "icon": "code-o",
            "color": "gray",
            "project_type": "private"
        }
        cj = s.post(url, data=data)
        group_id = (cj.json()['data']["_id"])
        print(cj.json())
        self.current_group_id = group_id
        return cj.content.decode('utf-8'), group_id

    def test_delete(self):
        url = "http://59.110.63.111:3000/api/project/del"
        groupid = self.current_group_id
        data = {'id': groupid}
        delect = s.post(url, data=data)
        print(delect.json())
        return delect.json()


if __name__ == "__main__":
    s = requests.session()
    blog = Test_Blog(s)
    c = blog.test_login()
    blog.test_chuangjian()
    blog.test_delete()
