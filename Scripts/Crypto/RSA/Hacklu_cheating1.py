from Crypto.PublicKey import RSA
import gmpy2

# Alice's public encryption parameters
n1 = long(1696206139052948924304948333474767)
e = long(65537)

# Bob's
n2 = long(3104649130901425335933838103517383)

# Yes! We can factorize the n
p1 = 38456719616722997
q1 = 44106885765559411

p2 = 49662237675630289
q2 = 62515288803124247

# that means we can find the decryption exponent d
phi1 = (p1-1)*(q1-1)
phi2 = (p2-1)*(q2-1)
d1 = long(gmpy2.invert(e, phi1))
d2 = long(gmpy2.invert(e, phi2))

# now construct the RSA with all the parameters
rsa1 = RSA.construct( (n1, e, d1) )
rsa2 = RSA.construct( (n2, e, d2) )

# and decrypt the messages from a pcap file!
from pcapfile import savefile

cf = savefile.load_savefile(open("bob_alice_encrypted.pcap"))

output = {}

for p in cf.packets:
    pack = str(p.packet)[136:].decode('hex').decode('base64')
    if 'DATA' in pack:
        seq = int(pack.split(';')[0].split(' ')[2])
        data = pack[16:].split(';')[0][:-1]
        sig = long(pack.split(';')[2].split(' = ')[1], 16)
        m = long(data, 16)
        decrypted = rsa2.decrypt(m)
        sigcheck = rsa1.sign(decrypted, '')[0]
        val = str(hex(decrypted)).strip('0x').rstrip('L').zfill(2).decode('hex')
        if sig == sigcheck:
            output[seq] = val
print ''.join(output.values())
