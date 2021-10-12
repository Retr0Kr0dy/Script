__author__ = 'RetR0'

import os

i = 1
j = 1
cwd = os.getcwd()
a = ("1")
b = a
fn = (b + (".py"))
c = ("1")

while j < 110:

    z = (c + "1")
    i = 1
    os.mkdir(r"C:\Users\...\Desktop\ " + c)

    while i < 110:
        d = (r"C:\Users\...\Desktop\ " + c)
        cwd = os.getcwd()
        fx = a + fn
        
        src = os.path.join(cwd, fn)
        dst = os.path.join(d, fx)

        from shutil import copyfile

        copyfile(src,dst)
        
        a += ("1")
        i += 1
        print (d)

    else:
        print (a)
    a = ("1")
    i = 1
    j += 1
    c += ("1")

