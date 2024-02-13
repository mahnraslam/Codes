
def pattern(n):
    i=0
    s=0
    while i<n:
        j=0
        while j <= i:
            print(s%10,end="")
            s=s+1
            j+=1
        print()
        i+=1

pattern(11)
'''for j in range(13):
    if j==11:
      print("skip the iteration")
      continue
    print("5 x",j,"=",5*j)
j=0
while j<13:
    j=j+1
    if j==10:
        continue
    print("5 x",j,"=",5*j)
'''


def  char(a):
  i=0
  c=""
  b=[0]*len(a)
  while i<len(a):
       z=a[i]
       s=chr(ord(z)-ord("a")+ord("A"))
       c=c+s
       i+=1
  print(c)
a= "iqbal"
char(a)
def isSquare(a):
    s=int(a**0.5)
    r=s*s
    if r==a:
        print(a)
def main():
    i=2
    j=0
    while j<50:
        if i==isPrime(i):
            return i
        i+=1
        j+=1
main()
def isPrime(a):
    i=2
    j=1
    while j<=50:
        s=int(i**0.5)
        r=s*s
        if r==i:
            print(i)
            j=j+1
        i+=1
isPrime(50)
