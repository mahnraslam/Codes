def RightShift(a, n):
    i = 0
    s = ""
    while i < n:
        s = s + chr(32)
        i = i + 1
    j=n
    while j < len(a):
        s = s + a[j]
        j = j + 1
    return s
print(RightShift("knowledge",4))
'''def pad(a,s,n):
    i=0
    z=s-len(a)
    s=""
    while i<z:
        s=s+str(n)
        i=i+1
    j = 0
    while j < len(a):
        s = s + a[j]
        j = j + 1
    return s
a="342231"
print(pad(a,10,0))'''
def coppiedArr(a,s1,tg):
    i=0
    s=""
    while i<len(a):
        s=s+a[i]
        i+=1
    k=len(a)
    while k<tg:
        s=s+chr(32)
        k+=1
    r=""
    n=s1
    while n<len(a):
        r=a[n]
        s=s+r
        n=n+1
    return s
print(coppiedArr("xdvffr",3,8))







