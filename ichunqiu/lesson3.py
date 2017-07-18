import requests
import re
from bs4 import BeautifulSoup as bs
import threading
import Queue
import urllib


url='http://jiandan.net/pic//page-2162#comments'

class Jiandan(threading.Thread):
	def __init__(self,queue):
		threading.Thread.__init__(self)
		self._queue = queue

	def run(self):
		while not self._queue.empty():
			url = self._queue.get_nowait()
			self.spider(url)

	def spider(self,url):
		headers = {'User-Agent':'jiandan spider by ichunqiu ado ver=1.0'}

		r =requests.get(url=url,headers=headers)

		'''
		imgs = re.findall('<img src="(.*?)" /></p>',r.content)
		for img in imgs:
			print img

		gifs = re.findall('org_src="(.*?)" onload=',r.content)

		for gif in gifs:
			print gif
		'''
		soup = bs(r.content,'lxml')
		imgs = soup.find_all(name='img',attrs={})

		for img in imgs:
			if 'onload' in str(img):
				img =  img['org_src']
			else:
				img = img['src']
			name = img.split('/')[-1]
			#print name
			urllib.urlretrieve(img,filename='img/'+name)

def main():
	queue = Queue.Queue()
	for  i in range(2159,2162):
		queue.put('http://jiandan.net/pic/page-2162'+str(i))

	threads = []
	thread_count = 5

	for i in range(thread_count):
		threads.append(Jiandan(queue))

	for t in threads:
		t.start()
	for  t in threads:
		t.join()
if __name__ == '__main__':
	main()