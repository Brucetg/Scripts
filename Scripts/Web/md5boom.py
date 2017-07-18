#!/usr/bin/env python
#-*- coding:utf-8 -*-
import hashlib
zidian= '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
while(True):
	for i in zidian:
		for j in zidian:
			for k in zidian:
				for m in zidian:
					for n in zidian:
						key = str(i)+str(j)+str(k)+str(m)+str(n)+'UxmGLoE40t'
						print key
						test = hashlib.md5(key).hexdigest()
						if test.startswith('7fc1'):
							print '[!]', 'found:', key,test
							break
	


