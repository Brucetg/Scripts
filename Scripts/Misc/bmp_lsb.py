# -*- coding: utf8 -*-
#最低位的亲吻
from PIL import Image
def foo():
    im=Image.open('misc_150.bmp')
    im2=im.copy()

    pix=im2.load()    #加载bmp图片的数据区
    width,height=im2.size

    for x in xrange(0,width):
        for y in xrange(0,height):
            #LSB
            if pix[x,y]&&(0x1)==0:  #获取最后一位
                pix[x,y]=0 #黑
            else:
                pix[x,y]=255
    im2.show()
    pass

if __name__ == '__main__':
    foo()
    print 'ok'
    pass
