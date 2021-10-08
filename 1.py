import os

i = 1
j = 1
cwd = os.getcwd()
a = ("1")
b = a

fn = (b + (".py"))

c = ("1")

while j < 210:

    z = (c + "1")

    os.mkdir(r"C:\Users\....\Desktop\ " + c)
    i = 1
    #d = (r"C:\Users\.....\Desktop\ " + c)
    while i < 210:
        d = (r"C:\Users\....\Desktop\ " + c)
        cwd = os.getcwd()
        fx = a + fn
        #print (fn)
        #print (fx)
        src = os.path.join(cwd, fn)
        dst = os.path.join(d, fx)

        from shutil import copyfile

        copyfile(src,dst)
        

        #if i == 227:
        #    break
        a += ("1")
        i += 1
        print (d)

    else:
        print (a)
    a = ("1")
    #if j == 227:
    #    break
    i = 1
    j += 1
    c += ("1")
#c += ("1")
print (c)
