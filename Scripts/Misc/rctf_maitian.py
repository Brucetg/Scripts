print bin(int(open("msg.txt","r").read(),16))[2:].replace("0",".").replace("1","#")
