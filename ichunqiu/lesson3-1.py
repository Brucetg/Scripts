import requests
import threading
import Queue
from bs4 import BeautifulSoup as bs
import json
import time

'''
pages = http://www.seebug.org/vuldb/vulnerabilities?page=1

vul = https://www.seebug.org/vuldb/ssvid-15335

exchange = https://www.seebug.org/vuldb/exchange/15334 POST  {"type":"poc","anonymous":true}

down = https://www.seebug.org/vuldb/downloadPoc/15334


'''
headers = {
			'Host': 'www.seebug.org',
			'User-Agent': 'Mozilla/5.0 (Macintosh;Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0',
			'Accept': 'text/javascript,application/json,*/*;q=0.01',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language':  'zh-CN,zh;q=0.8',
			'Content-Type':'application/x-www-form-urlencoded; character=UTF-8',
			'X-CSRFToken':'n9VSa0aBVLp0FarY7CjIrEBny1EzKmPS',
			'X-Requested-With':'XMLHttpRequest',
			'Referer':'https://www.seebug.org/vuldb/ssvid-15228',
			'Cookie':'Cookie: __jsluid=56191bedfc1746d0d48a996c4a0fa426; csrftoken=n9VSa0aBVLp0FarY7CjIrEBny1EzKmPS; Hm_lvt_6b15558d6e6f640af728f65c4a5bf687=1491525648,1491528144,1491528176,1491528193; Hm_lpvt_6b15558d6e6f640af728f65c4a5bf687=1491528251',
			'Connection':'keep-alive',
		}

class SeebugPoc(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue= queue

	def run(self):
		while not self._queue.empty():
			url = self._queue.get_nowait()
			spider(url)

def spider(url):
	dic = {}
	dic['type']= 'poc'
	dic['anonymous'] = 'true'
	datas = json.dumps(dic)
	r = requests.get(url=url,headers=headers)
	#print r.status_code
	soup = bs(r.content,'lxml')
	vulids = soup.find_all(name='a',attrs={'class':'vul-title'})
	for vulid in vulids:
		print  vulid['href'].split('-')[-1],vulid['title']
		exchange_url = 'https://www.seebug.org/vuldb/exchange/'+vulid['href'].split('-')[-1]
		#print exchange_url
		
		exchange_r = requests.post(url = exchange_url,headers = headers,data=datas)
		print exchange_r.status_code,len(exchange_r.content),exchange_r.content
		time.sleep(2)

		if len(exchange_r.content) in [52,69]:
			down_url = 'http://www.seebug.org/vuldb/downloadPoc/'+vulid['href'].split('-')[-1]
			down_url = requests.get(url=down_url,headers = headers)
			f= open('poc'+vulid['href'].split('-')[-1]+'.py','w')
			f.write(down_r.content)
			f.close()

		time.sleep(2)

def main():
	queue = Queue.Queue()
	for i in range(2080,2588):
		queue.put('https://www.seebug.org/vuldb/vulnerabilities?page='+str(i))
	threads = []
	thread_count = 1

	for i in range(thread_count):
		threads.append(SeebugPoc(queue))
	for t in threads:
		t.start()
	for t in threads:
		t.join()

if __name__ == '__main__':
	main()