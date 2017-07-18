#coding:utf-8
import base64
import requests
import re
url = 'http://c.bugku.com/web6/'
a = requests.session()
r = a.get(url)
FLAG =  r.headers['flag']
p = re.match('(.*)(:)(.*)',base64.b64decode(FLAG))
print p
payload = {'margin':base64.b64decode(p.group(3))}
print payload
r = a.post(url,data=payload)
print r.text

