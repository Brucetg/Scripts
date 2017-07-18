s =""

s = s.decode('hex')

with open('flag.zip','wb') as f:
	f.write(s)

