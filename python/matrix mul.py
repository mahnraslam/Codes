a=[[2,-1],[1,12],[1,-2]]
b=[[2,-1,0],[1,2,-3]]
R1=len(a)
c1=3
r2=len(b)
c2=3
c=[[0 for j in range(c2)]for i in range(R1)]
i=0
while i<len(a):
    j=0
    while  j<c2:
        k=0
        while k< len(a) :
            l=0
            sum=0
            while l<r2:
                z=a[j][l]*b[l][k]
                sum=sum+z
                l=l+1
            c[j][k]=sum
            k+=1
        j+=1
    i+=1
print(c)


a=[[1,2,3],[4,5,6]]
b=[[10,11],[20,21],[30,31]]
R1=len(a)
c1=3
r2=len(b)
c2=2
c=[[0 for j in range(c2)]for i in range(R1)]
i=0
while i<R1:
    j=0
    while  j<c2:
        l=0
        sum=0
        while l<r2:
            z=a[i][l]*b[l][j]
            sum=sum+z
            l=l+1
        c[i][j]=sum
        j+=1
    i+=1
print(c)












