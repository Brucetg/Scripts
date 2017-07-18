#coding:utf-8
from PIL import Image

lena = Image.open('Lena.png')
b0 = ''
bnum = 0
width,height = lena.size
for x in xrange(width):
	for y in xrange(height):
		if lena.getpixel((x,y)) != (255,255,0):
			if (lena.getpixel((x,y))[2] & 0x01):
				b0 += '\x00\x00\x00'
			else:
				b0 += '\xff\xff\xff'
			bnum += 1
print len(b0)
mode = 'RGB'
im = Image.frombuffer(mode,(300,300),b0)
im.save('1.bmp')

