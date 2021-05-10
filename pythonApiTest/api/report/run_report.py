# 找到最新测试报告
import smtplib  # 发送邮件模块
import time  # 等待
import unittest  # 框架
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(BASE_DIR)
sys.path.append(BASE_DIR)
from email.header import Header  # 定义邮件标题
from email.mime.text import MIMEText  # 定义邮件内容
from api.report.HTMLTestRunner import HTMLTestRunner # 测试报告模板

# 引用Use_Cases
from api.test.user_asserts import UserAsserts

#发送测试报告至指定邮箱
def send_mail(latest_report):
    f = open(latest_report, 'rb')
    email_content = f.read()
    f.close()
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名及密码
    user = 'll17681827772@163.com'
    password = 'BRKFCJFWLIEYOJMJ'

    # 发送邮箱
    sender = 'll17681827772@163.com'
    # 接受邮箱
    receives = ['1144767408@qq.com']

    # 发送邮件主题和内容
    subject = 'WEB api自动化测试报告'

    # HTML 邮件正文
    msg = MIMEText(email_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # HELO 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("开始发送邮件...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("邮件发送完成！")


# 找到最新的测试结果
def latest_report(localpath):

    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    lists = os.listdir(localpath)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(localpath + '/' + fn))
    print("latest report is :" + lists[-1])

    # 输出最新报告的路径
    file = os.path.join(localpath, lists[-1])
    return file


# 执行测试用例
if __name__ == '__main__':

    # 按类加载全部testxxx测试用例
     suite = unittest.TestSuite()
     suite.addTest(UserAsserts('test_userExchangeBalanceList'))
## 打印测试用例结果
     # result = unittest.TestResult()
     # unittest.registerResult(result)
     # testresult = suite.run(result)
     # print(testresult)


     now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
     localpath = os.getcwd()
     print("本文件目录位置：" + localpath)
     filepath = os.path.join(localpath, now + "api自动化测试报告.html")
     print("报告存放路径  ：" + filepath)

    # 打开文件位置，如果没有则新建一个文件
     with open(filepath,'wb') as f:
         runner = HTMLTestRunner(stream=f, title="api自动化测试报告")
         runner.run(suite)
     f.close()

    # 获取最新测试报告
     latest_report = latest_report(localpath)
    # 发送邮件报告
     send_mail(latest_report)

     print('已生成测试报告')







