#SIOC only!
#-*- coding:utf-8 -*-
__author__ = 'JayQiu'

import time
import requests
import re

class Login:

    #初始化
    def __init__(self):
        #检测间隔时间，单位为秒
        self.every = 10

    #模拟登录
    def login(self):
        print self.getCurrentTime(), u"连网中..."

        url="http://192.168.0.18:8080/portal/pws?t=li"
        #消息头
        headers={
        'Host': "192.168.0.18:8080",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
        'Accept': "text/plain, */*; q=0.01",
        'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        'Accept-Encoding': "gzip, deflate",
        'Referer': "http://192.168.0.18:8080/portal/templatePage/20150513150749195/login_custom.jsp",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'X-Requested-With': "XMLHttpRequest",
        'Content-Length':"382",
        'Connection': "close"
        }
        #提交的信息
        payload={
        'userName': 'YOUR_USER_NAME',
        'userPwd': 'YOUR_PASSWORD',
        'userurl': '',
        'portalProxyIP': '192.168.0.18',
        'portalProxyPort': '50200',
        'dcPwdNeedEncrypt': '1',
        'assignIpType': '0',
        'appRootUrl': 'http%3A%2F%2F192.168.0.18%3A8080%2Fportal%2F',
        'manualUrl': 'http%3A%2F%2Fwww.sioc.ac.cn',
        'manualUrlEncryptKey': 'dncQxn6R04R5qMPHtteayw%3D%3D'
        }
        try:
            r=requests.post(url,headers=headers,data=payload)
            print self.getCurrentTime(),u'连接内网成功，查看连接外网是否正常'
        except:
            print("error")
    #判断当前是否可以连网
    def canConnect(self):
        try:
            q=requests.get("http://www.baidu.com")
            m = re.search(r'STATUS OK', q.text)
            if m:
                return True
            else:
                return False
        except:
            print 'error'
            return False

    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #主函数
    def main(self):
        print self.getCurrentTime(), u"Hi，欢迎使用JayQiu的自动登陆程序"
        while True:
            self.login()
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print self.getCurrentTime(),u"断网了..."
                    self.login()
                else:
                    print self.getCurrentTime(), u"一切正常..."
                time.sleep(self.every)
            time.sleep(self.every)

login = Login()
login.main()
