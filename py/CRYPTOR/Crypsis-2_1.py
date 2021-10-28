__author__ = 'RetR0'

from hashlib import sha256
from os import urandom
import os
import hashlib
import blowfish

text = input ("text :")
output = input ("output file name :")
key = urandom(56)
iv = urandom(8)
hashnsalt = blowfish.Cipher(key)
with open (text, 'rb') as f_file_to_crypt:
    text_block = f_file_to_crypt.read()
    text_block_2 = bytes()
data_encryption = hashnsalt.encrypt_cfb(text_block_2, iv)

text_to_write = data_encryption.decode()
print (text_to_write)
# print (data_encryption)
# with open (output, 'wb') as f_output:
#      f_output.write(text_to_write)

# i = 0
# file_to_crypt = input ("file to crypt :")
# 
# word_key = ("70611ed00e1fa7da86f17bd15cf384569dd9d342b9810f1d359fd492022d328e1668505db7b1341084b0f06acfeca1f5de473b643544176f97589008693c0f19")
# # pre_keys = sha256(word_key.encode('utf-8')).digest()
# # hash_keys = hashlib.sha512(pre_keys)
# # hash_digest = hash_keys.hexdigest()
# # print (hash_digest)
# keys = sha256(word_key.encode('utf-8')).digest()
# with open (file_to_crypt, 'rb') as f_file_to_crypt:
#     text_block = f_file_to_crypt.read()
#     text_block_2 = bytes()
# for i in range (len(text_block)):
#     c = text_block[i]
#     j = i % len(keys)
#     b = bytes ([c^keys[j]])
#     text_block_2 = text_block_2 + b
# with open (output, 'wb') as f_output:
#     f_output.write(text_block_2)
# print (text_block)
# print (type(text_block_2))
