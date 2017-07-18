import urllib,json
from anonBrowser import *

def google(search_term):
	ab =anonBrowser()
	search_term = urllib.quote_plus(search_term)
	response = ab.open('http://gg2.firstguo.com/search?hl=zh-CN&site=webhp&source=hp&btnG=Google+%E6%90%9C%E7%B4%A2&q=' + search_term)
	object = json.load(response)
	print object
google('apple')