def isPalindome(a):
    r = ""
    for i in range(len(a)):
        j = len(a) - 1
        while j > i:
            if a[i] == a[j]:
                r = r + a[j]
            j -= 1
        i += 1
    k = len(r) - 2
    n = ""
    while k >= 0:
        n += r[k]
        k -= 1
    r = r + "" + n
    print(r)
isPalindome("character")
isPalindome("civic")
isPalindome("aibophobia")


def BestLine(x, y):
    sx = 0
    s2x = 0
    sy = 0
    sxy = 0
    n = len(x)
    i = 0
    while i < n:
        sx = sx + x[i]
        s2x = s2x + x[i] ** 2
        sy = sy + y[i]
        sxy = sxy + (x[i] * y[i])
        i += 1

    p = sxy - (sx * sy) / n
    q = (s2x) - ((sx) ** 2 / n)

    m = round(p / q, 3)
    c = round((sy / n) - (sx / n) * m)
    return f"y={m}x+{c}"


c = [1, 2, 3]
d = [1, 2.1, 2.9]
print(BestLine(c, d))
