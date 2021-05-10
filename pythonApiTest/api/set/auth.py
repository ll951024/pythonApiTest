#导包
import requests
import unittest
import json
import os

class Auth():
    def setUp(self):
        pass

    # 登录接口
    def auth(self, data):
        # 登录普通账号
        data = data
        headers = {
            'accept': "application/json, text/plain, */*",
            'client-type': "WEB",
            'accept-language':"zh-CN,zh;q=0.9",
            'content-type':"application/json;charset=UTF-8"
        }
        # 调用登录URL
        url = "http://www.longbit.pro/longbit/login"
        # 运行
        run = requests.post(url=url, data=data, headers=headers)
        self.runtest = run.json()

    # 获取登录auth
    def test_auth(self):
        # 调用登录(auth)方法
        data= {"mobile":"17812345678","nationCode":"86","code":"1234"}
        print(data)
        Auth.auth(self,json.dumps(data))
        # 将获取到的auth返回
        runtest = self.runtest
        run = runtest['data']['auth']
        return run

    def tearDown(self):
        pass

