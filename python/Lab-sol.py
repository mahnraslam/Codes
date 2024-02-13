def runLengthEncode(st):

    currentLoc = st[0]
    c = 0
    for j in range(len(st)):
        if st[j] == currentLoc:
            c = c + 1
        else:
            print(currentLoc,c,end="")
            currentLoc = st[j]
            c = 1
    print(currentLoc,c)

runLengthEncode("avcgggg***tuxxxxtrhy trhyugdtyhgt")


def centrePadding(st, ch, ln):
    for i in range(len(st)):
        leftPad = (ln - len(st)) // 2
        rightPad = ln - len(st) - leftPad
    return leftPad * (ch) + st + (ch) * rightPad

print(centrePadding("zara", "h", 12))

i = "$"
b = 4
print(b * i)


'''i = open("import.py", "r")
j = open("", "w")

c = i.read(1)
while c != "":
    if c > "a" and c < "z":
        c = chr(ord(c) - ord("a") + ord("A"))
    j.write(c)
    c = i.read(1)
i.close()
j.close()'''
