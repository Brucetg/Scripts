import base64
import requests

url = 'http://ctf5.shiyanbar.com/web/10/10.php'
flag = requests.get(url).headers['FLAG']
flag = base64.decodestring(flag).split(':')[1]
data = {"key":flag}
print requests.post(url,data).text
