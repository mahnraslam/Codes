def matrixform(a,row,col):
    for i in range(row):
        for j in range(col):
            k=i*col+j
            print(a[k],end="\t")
        print()
def main():
    a=[2,3,45,6,78,5,2,1,13,4,65,4,32,1,24,14,]
    s=matrixform(a,6,2)
    #m=matrixform(a,4,3)
    #n=matrixform(a,3,4)
    return s
main()
class array:
    pass
'''i=["banana","apple","orange"]      #lists
j={"favorites":"banana,""apple,""orange"}   #Dictionaries
fruits={"banana","apple","orange"}  #set
fruits.add("grapes")
fruits.add("apple")#Won't be added
print(fruits)
#Tuple
a=(6,90,7,5)#Tuple
print(a)'''

def get3Darray(a,page,row,col):
    tda=array()
    tda.s1=page
    tda.s2=row
    tda.s3=col
    tda.data=[None]*tda.s1*tda.s2*tda.s3
    return tda
def assign(ar,p,r,c,d):
    ar.data[p*ar.s2*ar.s3 + r*ar.s3 +c]=d
def main():
    a=[None]*4*3*2
    a=get3Darray(a,2,3,4)
    assign(a,1,2,3,66)
    assign(a,1,1,3,56)
    assign(a,1,1,2,66)
    assign(a,0,1,3,77)
    print(a.data)
main()

'''from random import randint
cities=["Lahore","karachi","sialkot"]
a=[[0 for c in range(8)]for r  in range(3)]
for r in range(3):
    sum=0
    print(cities[r],end="\t ")
    for c in range(8):
        a[r][c]=randint(11,33)
        print(a[r][c],end="\t")
        sum+=a[r][c]
    print()
    print("average is",sum//7)'''









