import mechanize

def testProxy(url,proxy):
	browser = mechanize.Browser()
	browser.set_proxies(proxy)
	page = browser.open(url)
	source_code = page.read()
	print source_code

url = 'http://ip.nefsc.noaa.gov/'
hideMeProxy = {'http':'103.229.127.58:80'}
testProxy(url,hideMeProxy)