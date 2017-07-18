from PIL import Image
from zlib import *
 
data = open('1.png','rb').read()[0xAC3:]
data = decompress(data)
 
img = Image.new('1', (25,25))
d = img.load()
 
for n,i in enumerate(data):
    d[(n%25,n/25)] = int(i)*255
 
f = open('2.png','wb')
img.save(f)
