#coding=UTF-8
def header():
    btype='424d' #头标识
    bsize='360c 3000' #大小
    bapp1='0000' #指定应用
    bapp2='0000' #指定应用
    boffset='3600 0000' #偏移量这里是54
    biSize='2800 0000' #位图信息头的大小40
    biWidth='5605 0000' #宽度，本题1366
    biHeight='0003 0000' #高度，本题768
    biPlanes='0100' #颜色平面数，总为1
    biBitCount='1800' #比特数/像素，本题24位
    biCompression='0000 0000' #压缩类型，0为不压缩
    biSizeImage='0000 0000' #图像的大小，本题多少无所谓
    biXPelsPerMeter='0000 0000' #水平分辨率，缺省
    biYPelsPerMeter='0000 0000' #垂直分辨率，缺省
    biClrUsed='0000 0000' #使用的颜色索引数，本题多少无所谓
    biClrImportant='0000 0000' #重要的颜色索引数，本题多少无所谓
    BMPheader=btype+bsize+bapp1+bapp2+boffset+biSize+biWidth+biHeight+biPlanes+biBitCount+biCompression
    BMPheader=BMPheader+biSizeImage+biXPelsPerMeter+biYPelsPerMeter+biClrUsed+biClrImportant
    return BMPheader.replace(' ','')
ciphertext=open('./misc_150.bmp','rb').read()
f=open('out.bmp','wb')
f.write(header().decode('hex')+ciphertext)
f.close()
