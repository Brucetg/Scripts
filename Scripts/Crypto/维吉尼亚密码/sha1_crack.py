import hashlib
import itertools
import string


def sha1(s):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(s)
    return sha1_hash.hexdigest()


def check(s):
    if s[0:7] == "619c20c" and s[8] == "a" and s[16] == "9":
        print("Find!")
        matched = True
        return matched

letters = itertools.product(string.printable, repeat=4)
for i in letters:
    password = "".join((i[0], "7", i[1], "5-", i[2], "4", i[3], "3?"))
    # print(password)
    hash = sha1(password.encode("utf-8"))
    if check(hash):
        print(password)
        break
