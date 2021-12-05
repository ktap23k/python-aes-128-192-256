#!/usr/bin/env python
# -*- coding: utf-8 -*-
import timeit
# import time
# t0 = time.time()
start = timeit.default_timer()
import aes, os
from base64 import b64encode
from base64 import b64decode

# key = os.urandom(16)
key = '1234567812345678123456781234567f'
key = bytes.fromhex(key)
# iv = os.urandom(16)
iv = b'1234567890123451'
# print(key,iv)

a = '1234'
# print('byte input: ',bytes.fromhex(a))
# print(str.encode(a,'UTF16'))
#
# inp = '001122'.encode('utf-8')
# print('input: ',inp)
inp = bytes.fromhex(a)
print(inp)
# inp = bytes.fromhex(a) # chuyển hex string to bytes, .hex() : chuyển bytes to hex()

encrypted = aes.AES(key).encrypt(inp)

print('encrypt: ',encrypted.hex())
# print(bytearray.fromhex(encrypted.hex()).decode('utf16'))

print('decrypt: ',aes.AES(key).decrypt(encrypted).hex())

stop = timeit.default_timer()
print('Time: ', stop - start)

# t1 = time.time()
# print(t1-t0)


def solve_bit(A, B):
    A = ''.join([str(bin(byte))[2:] for byte in bytearray(A, "utf8")])
    B = ''.join([str(bin(byte))[2:] for byte in bytearray(B, "utf8")])
    return sum([1 for i,j in zip(A,B) if i!=j])

