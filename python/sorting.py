a = [(23,13),(34,56),(21,1)]
for i in range(len(a)):
    pair =   a[i]
    if pair[0] > pair[1]:
          a[i] = (pair[1],pair[0])
print(a)
print(chr(49))



import datetime   as dt
def time():
    print(dt.datetime.now())
    return (dt.datetime.now())

def harry(n):
    if   approch == "i":
        if n==2:
            def harryExercise(n):
                f = open("where.txt", "a")
                f.write(str(time())+ n)
                print("succesfully written")
            n = input("enter exercise")
            harryExercise(n)
        elif n==1:
            def harryFood(n):
                f = open("where.txt","a" )
                f.write(str(time())+ n)
                print("succesfully written")
            n = input("enter food")
            harryFood(n)

    elif   approch=="r":
        if n==1:
            def harryExercise():
                f = open("where.txt", )
                print(f.read())
            harryExercise()
        elif n==2:
            def harryFood():
                f = open("where.txt", )
                print(f.read())
            harryFood()

def  john(n):
    if   approch == "i":
            if n==2:
                def johnExercise(n):
                    f = open("where.txt"," a")
                    f.write(str(time())+n)
                    print("succesfully written")
                n = input("enter exercise")
                johnExercise(n)
            elif n ==1:
                def johnFood(n):
                    f = open("where.txt","a" )
                    f.write(str(time())+ n)
                    print("succesfully written")
                n = input("enter food")
                johnFood(n)
    if   approch == "r":
            if n==1:
                def johnExercise():
                    f = open("where.txt" )
                    print(f.read())
                johnExercise()
            elif n ==2:
                def johnFood():
                    f = open("where.txt")
                    print(f.read())
                johnFood()
def main(f,n):
    f(n)
approch = input("enter i for iterative   and r for recurssive")
n = int(input("enter 1 for harry or 2 for john"))
i = int(input("enter 1 for food or 2 for exercise"))
if n==1:
    f = harry
else :
    f = john
main(f,i)






