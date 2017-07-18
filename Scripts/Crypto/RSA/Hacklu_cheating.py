import base64
import regex
packets = []
with open('stream.txt') as lines:
    for line in lines:
        decoded = base64.b64decode(line)
        match = regex.match(decoded).groups()
        seq = int(match[0])
        signature = int(match[2], 16)
        data = int(match[1], 16)
        data = bob.decrypt(data)
        if alice.verify(data, signature):
            data = chr(data)
            packets.append((
                seq,
                data,
                signature
            ))

print ''.join([packet[1] for packet in sorted(packets)])
