import unittest
import pymysql


class JDBC(unittest.TestCase):

# Longbit库
    """longbit库连接信息"""
    def JDBC_longbit(self):
        a = pymysql.connect(
            # 主机名或IP地址
            host="192.168.10.247",
            # 库名
            database="longbit",
            # 用户名
            user="root",
            # 密码
            password="0.123abc"
        )
        return a

    def db_longbit(self, sql):
        # 调用数据库连接信息
        connect = JDBC.JDBC_longbit(self)
        cursor = connect.cursor()
        # 调用SQL
        sql = sql
        cursor.execute(sql)
        # 获取并返回查询的结果
        result = cursor.fetchall()
        for da in result:
            self.data = da[0]
            # print(self.data)
            return self.data

    """用户质押信息表连接信息封装"""
    # contract_no 合约ID(所有)
    def test_db_longbit_contract_no(self):
        # 用户质押信息表最后一条数据
        JDBC.db_longbit(self, "select contract_no from User_pledge_info where user_id='103' and status='1' ORDER BY id DESC LIMIT 1;")
        data = self.data
        #print(data)
        # 返回查询的结果
        return data

        # contract_no 合约ID(活期)


    def test_db_longbit_contract_no_0(self):

    # 用户质押信息表最后一条数据
        JDBC.db_longbit(self, "select contract_no from User_pledge_info where user_id='103' and status='1' and periods_type='0' ORDER BY id DESC LIMIT 1;")
        data = self.data
        # print(data)
        # 返回查询的结果
        return data

        # contract_no 合约ID(定期)


    def test_db_longbit_contract_no_1(self):
    # 用户质押信息表最后一条数据
        JDBC.db_longbit(self, "select contract_no from User_pledge_info where user_id='103' and status='1' and periods_type='1' ORDER BY id DESC LIMIT 1;")
        data = self.data
        # print(data)
        # 返回查询的结果
        return data