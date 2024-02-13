assignGrade={90:'A'}
z=90
s=assignGrade[z]
print(s)


import array as arr             #array contain only one type of data
a = arr.array("i", [1, 3, 44])
print(a)

x=23453
y=4
print("{}".format(z))
print("%f"%z)
print("{:<+d}".format(z))
print("{:<+d}".format(z))
print("the value of b is {1} and a is {0} ".format(x,y))
print("the value of a is {:2d} and b is {:1.4f} ".format(x,y))
print("the value of a is {:<+4d} and b is {:12.4f} ".format(x,y))
print("the value of a is {:c>8d} and b is {:<12.4f} ".format(x, y))
print("the value of a is {:0>8d} and b is {:12.4f} ".format(x, y))

a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]

tgSum = 12
c=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]+b[j]==tgSum:
            c=c+1
print(c)

'''from random import randint
a=[[0]*50]*2
i = 0
while i < 2:
    sum = 0
    j = 0
    while j < 50:
        a[i][j] = randint(13,19)
        sum = sum+a[i][j]
        j += 1
    avg = sum//50
    #print("for ", a[i] ,"average is", avg)
    #print()
    i += 1
#print( round( 0.3435 , 2))
#print(pow(2, 2))
import sys
from random  import  randint
f=open("where.py","w")

for j in range(3):
    h=randint(14,34)
    i=str(h)+""+"\n"
    f.write (i)
f.close()
import sys as a
a.stdout.write("enter digits")
i=a.stdin.read(3)
j=a.stdin.read(4)
k=a.stdin.read(11)
print(i)
print(j)'''
i=0
j=1
k=0
while k<=50:
    #print(k)
    i=j
    j=k
    k=i+j

