c = open("misc_150.bmp","rb").read()[36:]
newfile = ""
for i in range(len(c)/2):
  first  = ord(c[2*i])   & 0xf;
  second = ord(c[2*i+1]) & 0xf;
  result = (first << 4) + (second)
  newfile += chr(result)
open("layer1.img","wb").write(newfile)

