def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

print decode('1100110 1101100 1100001 1100111 1111011 1010111 0110000 1010111 0101010 1100110 1110101 1101110 1101110 1111001 1111101')
