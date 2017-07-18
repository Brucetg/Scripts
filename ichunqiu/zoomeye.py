import requests
from bs4 import BeautifulSoup as bs

headers = {
	
		'Host': 'www.zoomeye.org',
		'Connection': 'close',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
		'Referer': 'https://www.zoomeye.org/search?t=host&q=tomcat',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Cookie': '__jsluid=ac135806c7a389881e6af8bdc2f8212a; Hm_lvt_e58da53564b1ec3fb2539178e6db042e=1491629893; Hm_lpvt_e58da53564b1ec3fb2539178e6db042e=1491632774; __jsl_clearance=1491634381.973|0|6EQBIMsoLimYAgChHHZjp3L8ApE%3D'
  		}
url =  'https://www.zoomeye.org/search?q=tomcat&t=host'
def spider(url):
	r = requests.get(url=url,headers=headers)
	soup = bs(r.content,'lxml')
	ips = soup.find_all(name='a',attrs={'class':'ip'})
	#for ip in ips:
	#	print ip.string

	ports = soup.find_all(name='i',attrs={'class':None})
	#print ports
	#for port in ports:
	#	print port.string.replace('\n','').replace(' ','')

	for ip,port in zip(ips,ports):
		print ip.string,port.string.replace('\n','').replace(' ','')

def main():
	for i in range(1,11):
		url = 'https://www.zoomeye.org/search?q=tomcat&t=host&p=10'+str(i)
spider(url)