from os import system
from os import SEEK_SET, SEEK_CUR, SEEK_END

f = open("where.txt","r+")
for i in range(300):
    f.write(str(i))

f.seek(0, SEEK_SET)
f.write("This message at 100 byte start\n")
for i in range(10):
    print(f.readline(19))
    print(f.readline(2))
f.seek(f.tell())
f.write("This message at 50 bytes ahead\n")


f.seek(0,SEEK_END)
f.seek(f.tell()-50)
f.write("This msg at 50 from last")
f.close()
