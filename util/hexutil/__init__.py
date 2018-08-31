import codecs
import re
import binascii
import struct

def encodeString(text):
    return addPrefix(str(binascii.hexlify(text.encode()), 'ascii').lower())

def decodeString(hex_str):
    return codecs.decode(stripPrefix(hex_str), 'hex')

def encodeToString(btext):
    return addPrefix(str(binascii.hexlify(btext), 'ascii').lower())

def encodeBytes(btext):
    return binascii.hexlify(btext)

def decodeBytes(bhex):
    return binascii.unhexlify(bhex)

def encodeBigInt(i):
    return i.to_bytes((i.bit_length() + 7) // 8 or 1, 'big')

def decodeBigInt(hex_str):
    return int(stripPrefix(hex_str), 16)

def encodeInt64(i):
    return i.to_bytes((i.bit_length() + 7) // 8 or 1, 'big')

def decodeInt64(hex_str):
    return int(stripPrefix(hex_str), 16)

# https://www.h-schmidt.net/FloatConverter/IEEE754.html
def encodeFloat64(f):
    return struct.pack('!f', f)

def decodeFloat64(hexstr):
    return struct.unpack('>f', bytes.fromhex(stripPrefix(hexstr)))[0]

def stripPrefix(text):
    return re.sub(r'^{0}'.format('0x'), '', text)

def addPrefix(text):
    return '0x'+stripPrefix(text)
