#导包
import unittest
import json
import requests
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(BASE_DIR)
sys.path.append(BASE_DIR)
from api.set.headers import Headers
from api.set.url import Longbit_Url
from api.set.jdbc import JDBC




class UserAsserts(unittest.TestCase):
    def setUp(self):
        pass

    #查询用户币币账户资产列表
    def test_userExchangeBalanceList(self):
        #url
        url = Longbit_Url.exchange_user_balance

        #Headers
        hearders = Headers.headers(self)

        #run
        run = requests.get(url=url,headers=hearders)
        result = run.json()
        totalAmount = result['data']['totalAmount']
        self.assertNotEqual(totalAmount,0,msg='测试失败时打印的信息')
        print(f'Success ： 币币账户totalBalance： {totalAmount}')

    #测试数据库连接
    def test_a(self):
        atest = JDBC.test(self)
        print(atest)





if __name__ == '__main__':

    unittest.main(verbosity=0)







