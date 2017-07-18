# -*- coding:utf8 -*-
__author__='pcat'
__blog__='http://pcat.cnblog.com'

import re

def print_exit(value):
    if type(value)==unicode:
        print(value)
    else:
        print(value.decode("utf-8"))
    exit()

try:
    import requests
except ImportError:
    print_exit("Error: you must install the requests.")

class pcat(object):
    def __init__(self):
        self.url=r'http://117.34.111.15:88/index.php?action='
        self.action,self._user='',''

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self,value):
        self._user=value

    def register(self):
        self.action='register'
        mydata={'user':self.user,'pwd':'pcat','submit':'Submit',}
        reply=requests.post(self.url+self.action,data=mydata)
        ok_status='alert("OK")'
        return ok_status in reply.content

    def login(self):
        self.action='login'
        mydata={'user':self.user,'pwd':'pcat','submit':'Submit',}
        #php里header("Location: ?action=home");这里requests得不允许重定向，不然拿不到cookies
        #否则得用requests.session()的request.headers来获取cookies
        reply=requests.post(self.url+self.action,data=mydata,allow_redirects=False)
        fail_status='Incorrect'
        if fail_status not in reply.content:
            sign=reply.cookies['sign']
            token=reply.cookies['token']
            return sign,token
        else:
            print_exit("登录不成功！")

    def manage(self,sign,token):
        self.action='manage'
        #text是backup.txt里内容
        #iv是由backup.txt的创建时间去计算得到的，记得用linux的php 64位去计算
        mydata={
            'do':'decrypt',
            'text':'34018770e87f5195923a434ce1a8bb9defe76053fff2ea04af6adb70e3f7d3792f22889951bec6dddf32cfaa7a33d4a3',
            'iv':'516664694c6936513870656f55373270',
        }
        mycookies={'sign':sign,'token':token,}
        reply=requests.post(self.url+self.action,data=mydata,cookies=mycookies,allow_redirects=False)
        ok_status='Secret Area'
        if ok_status in reply.content:
            myre=r'<h2>Secret Area</h2>[/ \t\r\n]*(.*)<br />'
            rst=re.findall(myre,reply.content)[0].decode('hex')
            padding=int(ord(rst[-1]))
            flag=rst[:-1*(padding)]
            print(flag)
        else:
            print_exit("O.O可能是哪里出错了吧？")

    pass


if __name__ == "__main__":
    #随便写个非空的用户名，但要求没被注册过
    user='随便你写什么字符串都可以！！！'
    p=pcat()
    p.user=user
    if not p.register():
        print_exit("请注册一个新用户！")      
    sign,token=p.login()

    #计算padding
    BS=16
    add_len=len('|1|'+sign) #35
    pad_len=BS-(len(user)+add_len)%BS
    padding=chr(pad_len)*pad_len
    CLEN=len(user)+add_len+pad_len

    p.user='%s|1|%s%s' %(user,sign,padding)
    if not p.register():
        print_exit("请注册一个新用户！")
    sign_x,token=p.login()

    #token取CLEN*2的长度（因为token是十六进制的）
    p.manage(sign,token[:CLEN*2])
    print("ok")
