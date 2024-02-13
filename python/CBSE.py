f = open("where.txt","r+")
f.seek(0)
f.write("Tip\n")
print(f.read())
f.close()
x = [1,2,3,4,5,6]
listY = [1,3,6,5,8,7,1,4,2]
for i in x:
    c = 0
    for y in listY:
        if i==y:
            c =c+1
    print(i,"count:",c,",",end="")

import io
sio = io.StringIO("Zero line.\n")
contents = sio.getvalue()
# print("0:", contents, "|")
# contents = sio.read(5)
sio.seek(18)
sio.write(" Fourth line.\n")
contents = sio.getvalue()
print(contents)
sio.close()

class studentInfo:
    pass
a = 1000000001, 1000000002, 1000000003, 1000000004, 1000000005
print(a)
def main():
    info = []
    i = 0
    while i < 2:
        info.append(studentInfo())
        info[i].name = input("enter:")
        info[i].id = input("id")
        info[i].address = input("enter address:")
        i += 1
    print(info[1].name)
    # print("student 2 is", (callStu(info,1)))
main()
[[2,3,4],[2,3,5],[6,4,5]]
