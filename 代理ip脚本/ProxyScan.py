#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-18 15:14:55
# @Author  : River 
# @Link    : http://www.blogsir.com.cn
# @Version : v2.0

import requests
from bs4 import BeautifulSoup as bs
import re
import Queue
from threading import Thread
import time
import random

proxy_file = 'proxy.txt' #代理ip
Q = Queue.Queue()
thread_count = 50  #可修改线程大小
target = 'http://m.fm12718902.icoc.me/nd.jsp?mid=310&id=17&groupId=0&typeList=%5B0%5D'

with open('ua.txt') as ff:
	headers_content = ff.readlines()

def proxy_spider():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
	url = 'http://www.xicidaili.com/nn'
	html = requests.get(url,headers=headers)
	print html.encoding

	soup = bs(html.content,'lxml')
	datas = soup.find_all(name='tr',attrs={'class':re.compile('|[^odd]')})
	for data in datas:
		soup_proxy_content = bs(str(data),'lxml')
		soup_proxys = soup_proxy_content.find_all(name='td')
		#print soup_proxys[1].string,soup_proxys[2].string,soup_proxys[5].string
		ip = str(soup_proxys[1].string)
		port = str(soup_proxys[2].string)
		types = str(soup_proxys[5].string)
		# print types,ip+":"+port
		proxy_check(ip,port,types)



def proxy_check(iport):
	proxy = {}
	proxy['http'] = '%s'%(iport)
	try:
		r = requests.get('http://1212.ip138.com/ic.asp',proxies=proxy,timeout=3)
		res = re.findall('\[.*?\]',r.text)
		if '124.127.193.120' in res[0]:
			print 'failed'
		else:
			print 'success',iport
			urls.append(iport)

	except Exception,e:
		# print e
		pass
		
def proxy_scan(ip):
	header = headers_content[random.randint(0,len(headers_content))].strip()
	headers = {'User-Agent': header}
	proxy = {}
	proxy['http'] = ip
	try:
		res = requests.get(url=target,headers=headers,proxies=proxy,timeout=3)
		print res.status_code
	except:
		pass 
			

def fuzzone():
	while True:
		try:
			ip = Q.get(True,1)
			proxy_scan(ip)
		except Exception,e:
			break 


def main():
	while True:
		with open(proxy_file) as f:
			for i in f:
				Q.put(i.strip())

		threads = [Thread(target=fuzzone,args=()) for i in range(thread_count)]
		for t in threads:
			# t.setDaemon(True)
			t.start()
		for t in threads:
			t.join()
		if Q.empty():
			print 'time sleep ten'
			time.sleep(10)



if __name__ == '__main__':
	main()