def decSys(a):
    i=0
    sum=0
    s=str(a)
    while i<len(s):
        q=a%10
        r=q*(8)**i
        sum=sum+r
        a=a//10
        i=i+1
    return sum
print(decSys(234))
def decSys(a):
    s=str(a)
    sum=0
    i=len(s)-1
    while i>=0:
        q=a//10**(i)
        r=q*(8)**i
        sum=sum+r
        a=a%10**i
        i=i-1
    return sum
print(decSys(234))


from math import log
def base(n,b):
    l=int(log(n,b))
    i=0
    while (l+1)!=0:
        q=n//b**l
        r=n%b**l
        print(q,end="")
        n=r
        l=l-1
        i+=1
def main():
    a=[2,43,44,64]
    s=[0]*4
    i=0
    while i<len(a):
        s[i]=base(a[i],2)
        print()
        i+=1
    return s
main()
print()


''' gpa(pf,pf_lab,ict):
  gra_sys={"a":5,"b":4,"c":3}
  pf_m=3*gra_sys[pf]
  ict_m=3*gra_sys[ict]
  pf_l=3*gra_sys[pf_lab]
  t0tal=pf_m+ict_m+pf_l
  return t0tal//9
print(gpa("a","a","b"))'''
'''a=[3,6,7,5,3,2,1,9,5,3,2,9]
max_dif=a[1]-a[0]
for i in range (2,len(a)):
    z=a[i]-a[i-1]
    if z>max_dif:
        max_dif = z
        c=i
print(max_dif,c)'''
def decendingOrder(a):
    i=0
    r=False
    while i<len(a):
        j=i
        while j<len(a):
            if a[i]>a[j]:
                r=True
            j+=1
        i+=1
    print(r)
s=[44,33,22,11]
decendingOrder(s)






