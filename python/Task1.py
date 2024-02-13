def main():
    f = open("Grades.txt", "r+")
    file = open("mistakes.txt", "w")
    error = 0
    f.readline()
    f.readline()
    sizeR_No = 10
    sizeName = 30
    sizeCrs = 6
    sizeMd = 2
    sizeSs = 2
    sizeFn = 2
    lineNo = 3
    for line in f:
        rNo = line[0:sizeR_No]

        if len(rNo) < 10:
            file.write("line num:" + str(lineNo) + line + "\n")
            error += 1
        name = line[sizeR_No+1: 40]
        i = sizeR_No + sizeName+1
        crs = line[i:i+sizeCrs]

        if len(crs.strip()) < 2:
            file.write("line num:" + str(lineNo) + line + "\n")
            error += 1


        i = sizeR_No + sizeName+2+ sizeCrs
        Md = line[i: i+sizeMd]
        if len(Md.strip()) < 1:
            file.write("line num:" + str(lineNo) + line + "\n")

        else:
            if int(Md) <= 0 or int(Md) > 99:
                error = error

            elif Md=="AB":
                file.write("line num:" + str(lineNo) + line + "\n")
                error+=1
        i = sizeR_No + sizeName+2+ sizeCrs + sizeMd + 1
        Ss = line[i : i+sizeMd]
        if len(Ss.strip()) < 1:
            file.write("line num:" + str(lineNo) + line + "\n")
            error += 1
        elif Ss=="AB":
            file.write("line num:" + str(lineNo) + line + "\n")


        i = sizeR_No + sizeName +2+sizeCrs + sizeMd + sizeSs + 2
        Fn = line[i  : i + sizeFn]
        if len(Fn.strip()) < 1:
            file.write("line num:" + str(lineNo) + line + "\n")

        else:
            if int(Fn) <= 0 or int(Fn) >= 99:
                error = error
            elif Fn=="AB":
                file.write("line num:" + str(lineNo) + line + "\n")
                error+=1
        lineNo += 1
    print(error)
    file.close()
    f.close()
    return


main()
