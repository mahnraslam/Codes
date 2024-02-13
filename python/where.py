client_names = {1:"harry",2:"john", 3:"dewar"}

for key,value in client_names.items():
    print("enter",key,"for", value)

z = client_names.items()
for i in z:
    pass
    #print("enter",i[0] , "for",i[1])
client_names = ["harry","john","dewar"]
for i,value in enumerate(client_names):
    print(i,value)

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(lambda n :n>"", list1))
print(res)
list1 = [10, 40, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
c= [1,2]
list1[2][2].extend(c)          #here append fun is necessary bcz index for already availabel item
print(list1)


def numbers():
    a = 23
    def num2():
        nonlocal a
        a = 32
        return a
    print(num2())
    return a
a = 12
print(numbers())
print(a)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
newlist = []
for i in range(len(list1)):
    for j in range(len(list2)):
        newlist.append(list1[i]+list2[j])
print(newlist)



def pattern(size):
    selectedList = [0,2,4,9]

    for i in range(size):
        if i in selectedList:
            print("+",end="")
            for j in range(5):
                print("/\\",end="")
            print("+")
        elif i == 3:
            for j in range(5):
                print("  ",end="")
            print()
        else:
            print("|",end="")
            for j in range(5):
                print(" "*2,end="")
            print("|")

pattern(0)

'''
for i in range(1,11):
    if i%2!=0:
        print("+",end="")
        for j in range(5):
            print("/\\",end="")
        print("+")
    else:
        print("|",end="")
        for j in range(5):
            print(" "*2,end="")
        print("|")

def checkerBoard(size):
    sqRoot = int(size ** 0.5)
    for i in range(size):
        for j in range(size):
            if i //  sqRoot % 2 == 0:
                if j //  sqRoot % 2 == 0:
                    z= sqRoot
                    print(z, end=" ")
                else:
                    z= 0
                    print((z), end=" ")
            else:
                if j  //  sqRoot % 2 == 0:
                    print(0, end=" ")
                else:
                    z = sqRoot
                    print(z, end=" ")
        print()
    print()
    for i in range(size):
        for j in range(size):
            if j % sqRoot % sqRoot == 0:
                z= sqRoot
                print(z, end=" ")
            else:
                if j % sqRoot// sqRoot  == 0:
                    z = 0
                    print(z, end=" ")

        print()
checkerBoard(16)
'''
