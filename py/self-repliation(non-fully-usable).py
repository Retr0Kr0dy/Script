__author__ = 'RetR0'

import os

i = 1
j = 1
cwd = os.getcwd()
a = ("1")
b = a

fn = (b + (".py"))

c = ("1")
d = ("\\")
f = (cwd + d + c)
g = (f + a)
print (f)

while j < 110:

    z = (c + "1")

    os.mkdir(f)
    #os.mkdir(r"C:\Users\...\Desktop\ " + c)
    i = 1
    #d = (r"C:\Users\...\Desktop\ " + c)
    while i < 110:
        #d = (r"C:\Users\...\Desktop\ " + c)
        cwd = os.getcwd()
        fx = a + fn
        #print (fn)
        #print (fx)
        src = os.path.join(cwd, fn)
        dst = os.path.join(g, fx)

        from shutil import copyfile

        copyfile(src,dst)
        

        #if i == 227:
        #    break
        a += ("1")
        i += 1
        print (f)
        c += ("1")

    else:
        print (a)
    c = ("1")
    a = ("1")
    #if j == 227:
    #    break
    i = 1
    j += 1
    c += ("1")
#c += ("1")
print (c)
