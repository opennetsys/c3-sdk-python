import os
from Crypto.Hash import SHA512
import hexutil

def new ():
    h = SHA512.new(data=os.urandom(8), truncate='256')
    return h.digest()

def hash (data):
    h = SHA512.new(data=data.encode(), truncate='256')
    return h.digest()

def hashToHexString (data):
    return hexutil.encodeToString(hash(data))

def equals (hexHash, data):
  return hexHash == hashToHexString(data)
