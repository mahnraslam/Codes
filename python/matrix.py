a=[7,0,9,8,8,6,4,5,2,3,5,6,7,5,6,7,7,5,4,2,6,9,7,5,4,3,4,4,8,5,6,7,8,6,5,5,8,8,9,4,3,8]
row=3
col=2
pages=2
file=2
for f in  range(file):                 #4D
    print("file",f)
    for i in range(pages):
        print("page",i)
        for m in range(row) :
            for j in range(col):
                k = f*pages*row*col + i*row*col+ m*col + j               #i*s2*s3*s4+i2*s3*s4+i3*s4+i4
                print(a[k],end="\t")
            print()
print()
for i in range(2):              #3D
    print("page",i)
    for m in range(row) :
        for j in range(col):
            k=i*3*2+m*2+j               #i*s2*s3*s4+i2*s3*s4+i3*s4+i4
            print(a[k],end="\t")
        print()
    print()
#for right up triangle
i=0
while i<6:
    j=0
    while j<=i:
        k= (i*(i+1)//2)+j              # i*i+1//2+j
        print(a[k],end="")
        j+=1
    print()
    i+=1
print()
# left side
i=0
c=0
size=6
while i<size:
    j=0
    while j<size-i:
        k=c+j
        print(a[k],end="")
        j+=1
    c=c+(size-i)
    print()
    i+=1

i=0
while i<6:
    m=0
    while m<5-i:
        print(chr(32),end="")
        m+=1
    j=0
    while j<=i:
        k= (i*(i+1)//2)+j              # i*i+1//2+j
        print(a[k],end="")
        j+=1
    print()
    i+=1
print()


i=0
c = 0
k = 0
while i<6:
    m=0
    while m<i:
        print(chr(32),end="")
        m+=1
    j=0
    while j<6-i:
        k = c+j                             # i*i+1//2+j
        print(a[k],end="")
        j+=1
    print()
    c=c+(size-i)
    i+=1
