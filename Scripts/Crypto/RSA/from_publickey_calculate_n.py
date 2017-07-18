from Crypto.PublicKey import RSA
key = RSA.importKey(open('public.key').read())
print key.n, key.e

