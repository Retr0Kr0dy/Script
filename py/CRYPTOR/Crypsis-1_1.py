__author__ = 'RetR0'

from hashlib import sha256

i = 0
file_to_crypt = input ("text to crypt :")
#crypted_text_block =
output = input ("file name :")
word_key = ("~|[{`~~~~[SRHT|DRFH~F\J`FJ[FRJ{RT~|R[Y{RG`Y~SRT[FY|S\TY(SRFTY-SFT_H`DF|[HJ~DR{J\|DR{YJD~RHDR\Y[|RTY~{RST[YSRT|Y`RTY[SRTY|RS~TY\RTY{YT~")
#word_key = input("key :")
keys = sha256(word_key.encode('utf-8')).digest()
#keys = sha256(word_key.encode('utf-16')).digest()

#with open (text_block_to_crypt) as f_text_block:
with open (file_to_crypt, 'rb') as f_file_to_crypt:
        with open (output, 'wb') as f_output:
            while f_file_to_crypt.peek():
                c = ord(f_file_to_crypt.read(1))
                j = i % len(keys)
                b = bytes ([c^keys[j]])
                f_output.write(b)
                i= i + 1
                
                
#version 1.1
