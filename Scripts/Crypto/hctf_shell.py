#!/usr/bin/env python
# coding:utf-8
__author__ = 'Aklis'
from Crypto import Random
from Crypto.Cipher import AES
import sys
import base64
def decrypt(encrypted, passphrase):
	IV = encrypted[:16]
	aes = AES.new(passphrase, AES.MODE_CBC, IV)
	return aes.decrypt(encrypted[16:])
def encrypt(message, passphrase):
	IV = message[:16]
	length = 16
	count = len(message)
	padding = length - (count % length)
	message = message + '\0' * padding
	aes = AES.new(passphrase, AES.MODE_CBC, IV)
	return aes.encrypt(message)
IV = 'YUFHJKVWEASDGQDH'
#message = IV + 'flag is hctf{xxxxxxxxxxxxxxx}'
#print len(message)
#example = encrypt(message, 'Qq4wdrhhyEWe4qBF')
#print example
#example = decrypt(example, 'Qq4wdrhhyEWe4qBF') 
#print example

a='mbZoEMrhAO0WWeugNjqNw3U6Tt2C+rwpgpbdWRZgfQI3MAh0sZ9qjnziUKkV90XhAOkIs/OXoYVw5uQDjVvgNA=='
b=base64.b64decode(a)
flag = decrypt(b,'Qq4wdrhhyEWe4qBF')
print b
print flag
