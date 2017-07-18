from scapy.all import *

interface = 'eth0'
probeReqs = []

def sniffProbe(p):
	if p.haslayer(Dot11ProbeReq):
		netName = p.getlayer(Dot11ProbeReq).info
		if netName not in probeReqs:
			probeReqs.append(netName)
			print '[+] Detected new Probe Request:' + netName
sniff(iface= interface,prn = sniffProbe)