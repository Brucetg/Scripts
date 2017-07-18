data = ''
with open('1.txt') as f:
    for i in f:
        data += i.decode('base64')

f1 = open('2.gif','wb')
f1.write(data[::-1])

f1.close()

