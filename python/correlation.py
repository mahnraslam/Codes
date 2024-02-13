def correlation(s,m):
    #a=[[0 for j in range (2)]for i in range(3)]
    i=0
    S1=3
    S2=3
    while i<len(m):
        j=0
        while j<S2:
            k=i
            p=0
            sum =0
            while k<i+S1:
                l=j
                q=0
                while l<j+S2:
                    z = s[k][l]*m[p][q]
                    sum=sum+ z
                    q=q+1
                    l+=1
                p=p+1
                k+=1
            s[i][j]=sum
            j += 1
        i += 1
    return s
s=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
m=[[1,2,3],[4,5,6],[7,8,9]]
print(correlation(s,m))
