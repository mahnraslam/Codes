def checkerBoard(size):
    sqRoot = int(size ** 0.5)
    for i in range(size):
        for j in range(size):
            if i // sqRoot % 2 == 0:
                if j // sqRoot % 2 == 0:
                    z="0"
                    print(z, end=" ")
                else:
                    z=sqRoot
                    print((z), end=" ")
            else:
                if j // sqRoot % 2 == 0:
                    z=sqRoot
                    print(z, end=" ")
                else:
                    z="0"
                    print(z, end=" ")
        print()
checkerBoard(9)


z = (11 // 4) % 2
print(z)

a = "I love my homeland"
print(a.strip("I love"))

from random import randint

"""f = open("", "r")
for i in range(4):
    a = f.readline().rstrip("\n")
    sum = 0
    for j in range(7):
        b = f.readline().rstrip("\n")
        sum = sum + int(b)
    print(f"department is {a} ", end=" ")
    print(f"expense is {sum}")
f.close()
from random import randint

f = open("hi.txt", "r")
department = ["Sales", "IT", "Production", "Bakery"]
totals = [0] * 4
for line in f:
    line = line.rstrip("\n")
    if line:
        if line in department:
            currentDept = department.index(line)
        else:
            totals[currentDept] += int(line)
f.close()
for i in range(len(department)):
    print(department[i], totals[i])


department=["Sales","IT","Production","Bakery"]
for f in department:
    print(f)"""
