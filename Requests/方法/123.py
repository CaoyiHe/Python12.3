1 # coding=utf-8
 2 # 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行
 3
 4 # 2.注释：包括记录创建时间，创建人，项目名称。
 5 '''
 6 Created on 2019-5-15
 7 @author: 北京-宏哥
 8 Project:学习和使用封装与调用--流程类接口关联
 9 '''
10 # 3.导入模块
11 import requests
12 # 禁用安全请求警告
13 import urllib3
14
15 urllib3.disable_warnings()
16 import warnings
17
18 warnings.simplefilter("ignore", ResourceWarning)
19
20
21 class Blog():
22     def __init__(self, s):
23         s = requests.session()  # 全局参数
24         self.s = s
25
26     def login(self):
27         '''登录接口'''
28         url = "http://localhost:8080/jenkins/j_acegi_security_check"
29         headers = {
30             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
31         }  # get方法其它加个ser-Agent就可以了
32         d = {"j_username": "admin",
33              "j_password": "111111",
34              "from": "",
35              "Submit": u"登录",
36              "remember_me": "on"
37              }
38
39         s = requests.session()
40         r = s.post(url, headers=headers, data=d)
41         # print (r.content.decode('utf-8'))
42         # 正则表达式提取账号和登录按钮
43         import re
44         t =Z re.findall(r'<b>(.+?)</b>', r.content.decode('utf-8'))  # 用python3的这里r.content需要解码
45         print(t[0])
46         print(t[1])
48     def get_postid(self, r2_url):
49         '''正则表达式提取'''
50         import re
51         postid = re.findall(r"postid=(.+?)&", r2_url)
52         print(postid)  # 这里是 list []
53         # 提取为字符串
54         print(postid[0])
55         return postid[0]
56
57     def save(self, title, body):
58         '''保存草稿箱：
59         参数 1：title # 标题
60         参数 2：body # 中文'''
61         url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
62         d = {"__VIEWSTATE": "",
63              "__VIEWSTATEGENERATOR": "FE27D343",
64              "Editor$Edit$txbTitle": title,
65              "Editor$Edit$EditorBody": "<p>%s</p>" % body,
66              "Editor$Edit$Advanced$ckbPublished": "on",
67              "Editor$Edit$Advanced$chkDisplayHomePage": "on",
68              "Editor$Edit$Advanced$chkComments": "on",
69              "Editor$Edit$Advanced$chkMainSyndication": "on",
70              "Editor$Edit$lkbDraft": "存为草稿",
71              }
72         r2 = self.s.post(url2, data=d, verify=False)  # 保存草稿箱
73         print(r2.url)
74         return r2.url
75
76     def del_tie(self, postid):
77         '''删除帖子'''
78         del_json = {"postId": postid}
79         del_url = "https://i.cnblogs.com/post/delete"
80         r3 = self.s.post(del_url, json=del_json, verify=False)
81         print(r3.json()["isSuccess"])
82         return r3.json()
83
84
85 if __name__ == "__main__":
86     s = requests.session()
87     Blog(s).login()