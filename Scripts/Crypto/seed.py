from __future__ import print_function
import random
import string

payload = string.printable[:-6]

def randstr():
	rstr = "".join([payload[random.randint(0,len(payload)-1)] for _ in range(16)])
	return rstr

for i in range(1,9999):
	random.seed(i)
	if i>1001:
		print('no')
		break
	if randstr() == r'$9jub6:hJ|[|PS#-':
		print(randstr())
		break
