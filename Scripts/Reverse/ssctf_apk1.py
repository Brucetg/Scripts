from zipfile import is_zipfile
from openpyxl import load_workbook
import StringIO
def getk(key):
    k = [50, 105, 20, 75, 40, 45, 1, 15, 98, 17, 68, 35, 38, 30, 8, 0, 76, 65, 46, 35, 23, 5, 120, 55, 90, 41, 60, 20,
         30, 117, 50, 87, 20, 57, 108, 27, 78, 61, 80, 8]
    for i in range(100):
        for j in range(100):
            k[(i + 17) * (j + 5) % len(k)] = (k[i * j % len(k)] ^ ord(key[i * j % len(key)]) * 7) % 127
    return k
enc_str = open('ctf1_encode.xlsx', 'rb').read()
enc_list = [ord(i) for i in enc_str]
def run():
    magic = enc_list[0] ^ ord('P')
    for key in xrange(100000, 1000000):
        k = getk(str(key))
        if k[0] == magic:
            l = list(enc_list)
            for j in range(0, len(l), 256):
                l[j] ^= k[j % len(k)]
            s = StringIO.StringIO(''.join([chr(i) for i in l]))
            if is_zipfile(s):
                print key
                try:
                    load_workbook(s)
                    print 'got it', key
                    open('tmp.xlsx', 'wb').write(''.join([chr(i) for i in l]))
                    return
                except:
                    continue
run()