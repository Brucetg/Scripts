import requests
import re
import time

PHPSESSID = 'nidioemqbver'
cookie = {'PHPSESSID':PHPSESSID}

def geturls():
	url = 'http://106.75.30.59:8888/game.php'
	refind = re.compile(r'(?<=<a href=").*(?=">&nbsp;)')
	r = requests.get(url,cookies=cookie)
	urllist = refind.findall(r.text)
	return urllist


if __name__ == '__main__':

	urllist = geturls()
	while(1):
		for i in urllist:
			print i
			requests.get('http://106.75.30.59:8888/'+i[2:],cookies = cookie)
			requests.get('http://106.75.30.59:8888/dorob.php',cookies = cookie)
		time.sleep(3)
