L = "!:#$%&()+-*/`~_[]{}?<>,.@^abcdefghijklmnopqrstuvwxyz012345678"
L = [ord(i) for i in L]
def enc(s):
    assert len(s) == 12
    l = [ord(i) for i in s]
    r = []
    for i in range(0, len(l), 3):
        r.append(L[
                     l[i] >> 2
                     ]
                 ^ 0x3f)
        r.append(L[
                     (
                         l[i + 1] >> 4
                     )
                     +
                     (
                         (l[i] << 4)
                         & 0x3f
                     )
                     ] ^ 0xf)
        r.append(L[
                     (
                         (l[i + 1] << 2)
                         & 0x3f
                     )
                     + (
                         l[i + 2] >> 6
                     )
                     ])
        r.append(L[
                     l[i + 2] & 0x3f
                     ])
    print r
    return ''.join([chr(i) for i in r])
s = enc('0123456789ab')
# print s
print len(s)
print s.encode('hex')
def dec(s):
    def index(j):
        return L.index(j)
    l = [ord(i) for i in s]
    r = []
    for i in range(0, len(l), 4):
        r.append(
            (
                (index(l[i] ^ 0x3f) << 2) & 0xff
            ) +
            (
                index(l[i + 1] ^ 0xf) >> 4
            )
        )
        r.append(
            (
                (index(l[i + 1] ^ 0xf) << 4) & 0xff
            ) +
            (
                index(l[i + 2]) >> 2
            )
        )
        r.append(
            (
                (index(l[i + 2]) << 6) & 0xff
            ) +
            index(l[i + 3])
        )
    print r
    return ''.join([chr(i) for i in r])
print dec(s)
print dec('01635e6c5f2378255f27356c11663165'.decode('hex'))
