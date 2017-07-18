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
						key = str(i)+str(j)+str(k)+'aITMpJ85vo'
						#print key
						test = hashlib.md5(key).hexdigest()
						
						if test.startswith('c58b'):
							print '[!]', 'found:', key,test
						break
	


