nums = []
keys = open('usbdata.txt','r')
out = open('data.txt','w')
posx = 60
posy = 10
for line in keys:
    # if len(line) != 12 :
         # continue
    x = int(line[6:8],16)
    y = int(line[12:14],16)
    # print x,y
    if x > 127 :
        x -= 256
    if y > 127 :
        y -= 256
    posx += x
    posy += y
    btn_flag = int(line[3:5],16)  # 1 for left , 2 for right , 0 for nothing
    if btn_flag == 1 :
        out.write( "%d %d\n"%(posx ,posy))
keys.close()
out.close()
