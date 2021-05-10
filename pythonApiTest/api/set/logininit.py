#导包
import requests
import json
import os
import unittest

class Init():

    def test_init(self):
        #-----------获取图形验证码--------
        url="https://www.longbit.pro/longbit/gt/init"

        headers ={
            "Content-Type": "from-data"
        }

        data ={
            "mobile": 17812345678,
            "nationCode": 86,
            "clientType": "WEB",
            "verifyType": "login"
        }

        r=requests.post(url,data)
        result = r.json()
        sequence = result['data']['sequence']
        return sequence



    def test_userlogin(self):
        #-----------白名单用户登录--------
        url = "https://www.longbit.pro/longbit/login"

        headers={
            "sequence": Init.test_init(self),
            "Content-Type": "application/json"
        }

        data ={
            "mobile": "17812345678",
            "nationCode": "86",
            "code": "1234"
        }
        r = requests.post(url=url,headers = headers,data=json.dumps(data))
        print(r)
        result = r.json()
        auth = result['data']['auth']
        return(auth)










