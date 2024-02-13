def inorganicChem(formula):
    print("Formula from inorganic chemistry",formula)
    return

def organicChem(formula):
    print("Formula from organic chemistry",formula)
    return

def runFunction(f,p):
    f(p)

formula=input("Enter formula")
n=int(input("Enter 1 if formula contain C  and H:"))
if n==1:
    fn = organicChem
else:
    fn= inorganicChem
runFunction(fn,formula)

while True:
    n=int(input("enter 1 or 8 to break"))
    if n==1:
        def add(a,b):
            print(a+b)
            return
        def subtract(a,b):
            print(a-b)
            return
        def multiply(a,b):
            print(a*b)
            return
        def devide(a,b):
            print(a/b)
            return
        def runFunction(f,a,b):
            f(a,b)
        num1=int(input("Enter num 1:"))
        num2=int(input("Enter num 2:"))
        i =int(input("Enter function 1 for add or 2 for subtract or 3 for multiplication or 4:"))
        if i==1:
            f=add
        elif i==2:
            f= subtract
        elif i==3:
            f=multiply
        elif i==4:
            f=devide
        runFunction(f,num1,num2)
    if n==8:
        break


import numpy as np

x = np.array([(1,2,3),(3,4,5)])
y = np.array([(1,2,3),(3,4,5)])

print(x-y)
print()
print(x*y)
print()
print(x/y)


f = open("01.txt", 'rb')
#text = [225, 97, 32, 13, 10, 65]

for s in  range(6):
    z=int.from_bytes(f.read(2),byteorder='big')
	# 4 is no of byte, big is big endian
	#f.write(s.to_bytes(2, byteorder='big',signed=True))
    print(z)
f.seek(0)
b=f.read(10)
while b:
    print(b)
    print(len(b))
    b = f.read(10)
print("============\nAfter EOF")
print(b)
print(len(b))
f.close()

'''f = open("01.txt", 'rb')
text = f.read()
print(text)
for s in text:
    print(s)'''

