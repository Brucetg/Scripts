# -*- coding:utf-8 -*-

import binascii
def crc32(v):
    return '%x' % (binascii.crc32(v) & 0xffffffff) 

def foo():
    chunk_type="49484452"
    chunk_data_model="000002A7 %s 08 06 00 00 00"
    chunk_crc_raw="6D7C7135"

    for i in xrange(0xffff):
        chunk_data=chunk_data_model %'{:08x}'.format(i)
        chunk_crc=(chunk_type+chunk_data).replace(' ','').decode('hex')
        if crc32(chunk_crc).upper()==chunk_crc_raw:
            print i,'{:08x}'.format(i)
            break
    pass

if __name__ == '__main__':
    foo()
    print 'ok'
