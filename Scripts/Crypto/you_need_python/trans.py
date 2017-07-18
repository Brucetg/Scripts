import utf9
a = open('2.txt', 'r')
b = a.read()
c = utf9.utf9decode(b)

num = 0
data= ''
for i in c:
    if i == '_':
        num += 1
    else:
        if num != 0:
            data += repr(num)
            num = 0
        data += i
data += repr(num)
print eval(data)