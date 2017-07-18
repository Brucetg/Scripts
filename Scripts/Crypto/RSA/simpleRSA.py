import gmpy2
N,p,q,e=920139713,18443,49891,19
d = gmpy2.invert(e,(p-1)*(q-1))
res = []
with open('RSAROLL.txt') as f:
	f.readline()
	f.readline()
	for i in f:
		res.append(chr(pow(int(i),d,N)))
print (''.join(res))

