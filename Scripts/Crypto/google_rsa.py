import os
import asn1
import requests
import base64
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes, size

def true_cbrt(n):
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo+hi)//2
        if mid**3 < n:
            lo = mid+1
        else:
            hi = mid
    return lo

def get_bit(n, pos):
    return (1 if (n & (1 << pos)) else 0)

message = "challenge"

key = RSA.importKey(open('adminpub.key').read())
h = MD5.new(message)
padded = PKCS1_v1_5.EMSA_PKCS1_V1_5_ENCODE(h, size(key.n)/8)

asn1hash = "\x00" + padded.split("\xff\xff\xff\x00")[-1]

asn1hash_l = bytes_to_long(asn1hash)

# find the value resulting in ASN.1 + hash suffix when cubed
sig_suffix = 1
for bit_pos in range(len(asn1hash) * 8):
    if get_bit(sig_suffix ** 3, bit_pos) != get_bit(asn1hash_l, bit_pos):
        sig_suffix ^= (1 << bit_pos) # flip the incorrect bit

if not long_to_bytes(sig_suffix ** 3).endswith(asn1hash):
    raise

print "Signature suffix found"
print

# combine the cube roots checking for null bytes
while True:
    prefix = bytes_to_long("\x00\x01" + os.urandom(1024/8 - 2))
    sig_prefix = long_to_bytes(true_cbrt(prefix))[:-len(asn1hash)]
    sig = sig_prefix + long_to_bytes(sig_suffix)
    if "\x00" not in long_to_bytes(bytes_to_long(sig) ** 3)[:-len(asn1hash)]:
        break

print "Full signature obtained"
print

print "Resulting padded message:"
print long_to_bytes(bytes_to_long(sig) ** 3).encode('hex')
print

sig = sig.rjust(128, "\x00")
sig = base64.b64encode(sig)
r = requests.post("http://pkcs-is-bad.ctfcompetition.com/check", json={"Signature":sig})
print r.text

