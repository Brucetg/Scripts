list = [23,22,26,26,25,25,25,26,27,28,30,30,29,30,32,32]
str = ''
temp = 0
for m in list:
	for i in range(255):
		n = ((i+m)%61)*2- temp
		if n == i:
			str += chr(n)
	temp += 1

print str
