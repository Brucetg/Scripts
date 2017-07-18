f = open ('reverseMe','rb')
w = open("rem.jpg",'wb')
x = f.read()[::-1]
w.write(x)

