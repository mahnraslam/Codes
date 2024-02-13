def pattern(n):
    i = 0
    while i <= n:
        j = n
        while j > i:
            s = " "
            if j >= 10:
                s = "  "
            print(s, end="")
            j = j - 1
        k = 0
        while k <= i:
            print(k, end="")
            k += 1
        print()
        i += 1


pattern(5)


def patterns(n):
    i = 0
    while i < n:  #''' s=0 print(s,end=""), if  s >= 10:   s=0
        j = 0
        while j <= i:
            print(j % 10, end="")
            j += 1
        print()
        i += 1


patterns(6)

from random import randint

a = [0] * 15
i = 0
while i < 15:
    a[i] = randint(12000, 1000000)
    i += 1


def salaries(a):
    i = 0
    r = None
    while i < 15:
        if a[i] >= 12000:
            r = "scale:1"
            if a[i] >= 50001:
                r = "scale:2"
                if a[i] >= 125000:
                    r = "scale:3"
                    if a[i] >= 400001:
                        r = "scale:4"
                        if a[i] >= 900000:
                            r = "scale:5"
        print(r)
        i = i + 1


salaries(a)


def mongeArray(a):
    s2 = 3
    r = True
    i = 0
    p = i + 1
    while i < len(a) - 1:
        j = 0
        q = j + 1
        while j < len(a) - 1:
            z = (a[i][j]) + (a[p][q])
            n = (a[i][q]) + (a[p][j])
            if z > n:
                r = False
            q = q + 1
            j = j + 1
        p = p + 1
        i = i + 1
    return r
a = [
    [10, 17, 13, 28, 23],
    [17, 22, 16, 29, 23],
    [24, 28, 22, 34, 24],
    [11, 13, 6, 17, 7]
    ]
print(mongeArray(a))
