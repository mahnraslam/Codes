sum=0
a=[[1,2,3,6],[5,6,5,9],[6,8,9,0]]

i=0
while i< 4:
    j=0
    while j<3:
        print(a[j][i],end=" ")
        j+=1
    print()
    i+=1

a=[[0]*7]*3
for i in range(3):
    s=0
    for j in range(7):
        a[i][j]=int(input("enter:"))
        s=s+a[i][j]
    print("for  city ",i , "is", end=" ")
    print(s//7)




i=0
while i<len(a):
    j=0
    while j<3:
        if i==j:
            sum=sum+a[i][j]
        j+=1
    i+=1
#print(sum)









