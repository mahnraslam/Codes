'''def numbers(a):
  i=0
  sum=0
  j=len(a)-1
  while i<len(a):
      if ord(a[i])>=ord("0") and ord(a[i])<=ord("9"):
        r=(ord(a[i])-ord("0"))*10**j
        sum=sum+r
        j=j-1
        i=1
  print(sum)
s="557"
print(numbers(s))
def lower(a):
  i=0
  s=""
  while i<len(a):
      if ord(a[i])>=ord("A") and ord(a[i])<=ord("Z"):
        s=s+chr(ord(a[i])-ord("A")+ord("a"))
      else:
          s=s+a[i]
      i+=1
  return s
print(lower("nAWAB"))
def proper(a):
  i=0
  s=""
  while i<len(a):
      if i==0 or ord(a[i-1])==32:
        if ord(a[i])>=ord("a") and ord(a[i])<=ord("z"):
          s=s+chr(ord(a[i])-ord("a")+ord("A"))
        else:
            s=s+a[i]
      else:
        s=s+a[i]
      i+=1
  return s
print(proper("abdul basit"))'''
'''def isPalindrome(a):
    i=len(a)-1
    s=""
    r=False
    while i>=0:
        s=s+a[i]
        i=i-1
    if s==a:
       r=True
    return r
print(isPalindrome("level"))
print(isPalindrome("brother"))
def join(s1,s2):
  c=""
  c=c+s1+s2
  return c
print(join("ba","ba"))'''
'''def substring(s,s1,s2):
  i=s1
  r=""
  while i<=s2:
      r=r+s[i]
      i+=1
  return r
s="I never want to see this moutain again...."
print(substring(s,3,23))'''
'''def trim(s):
  i=1
  a=""
  while i<len(s):
      if ord(s[i-1])==32 and ord(s[i])==32:
        a=a+""
      else:
          a=a+s[i]
      i+=1
  print(a)
trim("     such a good sweater    ")'''
def trim(a):
    s=""
    i=len(a)-1
    count=0
    z=-1
    while i > z :
        if ord(a[i])!=32:
             z=i
        count=count+1
        i-=1
    n=0
    l=len(a)
    while n < l:
        if ord(a[n])!=32:
             l=-1
             m=n
        n+=1
    k=m
    j=len(a)-count
    while k<=j:
        s=s+a[k]
        k+=1
    print( s, )
s="     such a good sweater        "
trim(s)

'''i=32
while i<127:
    z=chr(i)
    print(z,i,end=" ")
    i=i+1
k=0
while k<32:
    z=chr(k)
    print(z,k,end="")
    k=k+1
j=129
while j<257:
    s=chr(j)
    print(s,j,end="")
    j+=1'''




def arrays(a,n,sum,v):
  i=0
  count=0
  while i<n:
      if sum==a[i]+v:
        count+=1
      i=i+1
  return count
a=[2,3,45,6,1,3,4,5,7,887,7,7,3,2,4,1,78,3,1,887,33,556,2,1,1,32,12,13,887,16,18,10]
v=99
print(arrays(a,len(a),986,v))

































