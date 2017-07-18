import  string 
import hashlib
import re
zidian = string.printable
pattern = re.compile(r'619c20c.a4de755.9be9a8b.b7cbfa5.e8b4365.')

print len(zidian)
count = 0
for i in zidian:
	for j in zidian:
		for m in zidian:
			for n in zidian:
				count = count+1
				tmp = i + '7' + j + '5' +'-' + m + '4' + n + '3?'
sha1_value = hashlib.sha1(tmp).hexdigest()
if re.match(pattern,sha1_value):
	print tmp
if count%10000  == 0:
	print count