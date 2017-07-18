from pwn import *

r = remote('rsasign1.2017.teamrois.cn', 3000)
print r.recvuntil('\n')
r.send('\x00'*125)  # message with padding
print r.recvuntil('\n')
print r.recvuntil('\n')
r.send('00')  # signature
print r.recv(1024)
