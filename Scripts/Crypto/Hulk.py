#!/usr/bin/env python
# encoding: utf-8
from zio import *
flag = ''
target = ('202.112.51.217',9999)
dic = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}"
def get_payload(a, b, c):
    return ''.join(chr(ord(a[i]) ^ ord(b[i]) ^ ord(c[i])) for i in xrange(16))
def exp(i, payload):
    io = zio(target, timeout=5, print_read = COLORED(NONE, 'red'), print_write = COLORED(NONE, 'green'))
    io.read_until('encrypt: 0x')
    pay1 = '30' * (48-i)
    io.writeline(pay1)
    io.read_until('ciphertext')
    data = io.read_until('Give')
    io.read_until('encrypt: 0x')
    ciphertext1 = data[data.find('0x')+2:-5]
    data1 = ciphertext1[64:96]
    tmp = ('0' * (39 - len(flag + payload)) + flag + payload)[-16:]
    pay2 = get_payload(ciphertext1[32:64].decode('hex'), ciphertext1[-32:].decode('hex'), tmp).encode('hex')
    io.writeline(pay2)
    io.read_until("ciphertext")
    r2 = io.read_until("\n")
    ciphertext12 = r2[r2.find('0x')+2:r2.find('0x')+34]
    io.close()
    if data1 == ciphertext12:
        return 1
    else :
        return 0
for i in xrange(1, 39):
    for pay in dic:
        if exp(i, pay):
            flag += pay
            print flag
            break
print flag
