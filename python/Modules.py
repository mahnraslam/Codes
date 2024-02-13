from classVector import vector as vec

vec.x = 2
vec.y = 3
vec.z = 1
print(vec.magnitude(vec))
import datetime as dt

d = dt.date(2022, 12, 21)
#print(dt.date.today())
#print(d)
#print(dt.datetime.now().date() - d)
dif = dt.datetime.now().date() - d
print(dif.days)

t = dt.time(6, 37, 0)
#print(dt.datetime.now().time())
#print(t)
#print(dt.datetime.now().time() - t)
dif = dt.datetime.now() - dt.datetime.combine(dt.date.today(), t)
print(dt.datetime.now() - dt.datetime .combine (dt.datetime .today(),t))
print(dif.seconds)

import ctypes
ArrayType = ctypes.c_int * 5
slots = ArrayType()

for i in range(5):
    slots[i] =  10-i

for v in slots:
    print(v)

import datetime
x=datetime.datetime.now()
x = x.strftime("%Y")
print(x)
import struct
def half_image(f):
    f = open(f,"rb+")
    f.seek(18)
    w = "%s" %struct.unpack("i",f.read(4))
    h = "%s" %struct.unpack("i",f.read(4))
    f.seek(28)
    d = "%s" % struct.unpack("H", f.read(2))
    print("width=",w)
    print("height=",h)
    print("bits per pixel=",d)

    f.seek(54)
    a = [[[0,0,0] for i in range(int(w))] for j in range(int(h))]
    lc = int(w)*3  # count of bytes read on one scan line
    brl = lc % 4  # bytes peddings on scan line
    for i in range(int(h)-1,-1,-1):
        for j in range(int(w)):
            a[i][j][0] = int.from_bytes(f.read(1), byteorder ='big')  #"%s" % struct.unpack("b",f.read(1))
            a[i][j][1] = int.from_bytes(f.read(1), byteorder ='big')  #"%s" % struct.unpack("b",f.read(1))
            a[i][j][2] = int.from_bytes(f.read(1), byteorder ='big')  #"%s" % struct.unpack("b",f.read(1))
            lc += 3
        f.read(brl)

    f.seek(54)
    for i in range(int(h)-1,-1,-1):
        for j in range(int(w)//2):
            b = 255 - int(a[i][j][0])
            f.write(b.to_bytes(1, byteorder ='big'))
            b = 255 - int(a[i][j][1])
            f.write(b.to_bytes(1, byteorder ='big'))
            b = 255 - int(a[i][j][2])
            f.write(b.to_bytes(1, byteorder ='big'))
        for j in range(int(w)//2, int(w)):
            b = int(a[i][j][0])
            f.write(b.to_bytes(1, byteorder ='big'))
            b = int(a[i][j][1])
            f.write(b.to_bytes(1, byteorder ='big'))
            b = int(a[i][j][2])
            f.write(b.to_bytes(1, byteorder ='big'))
            #f.write(str(b).encode())
        f.write(int(0).to_bytes(brl, byteorder ='big'))

    f.close()

def main():
    print("You may create BMP files and pp.bmp is provided")
    print("You may run the code, twice to get rid of the effect of first run")
    file = input("Input the bmp file name with extension (.bmp): ")
    half_image(file)
main()










