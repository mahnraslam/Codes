def main():
    f = open("Grades.txt","r+")
    line = f.readlines()
    line[12]="BSSEF0M001 Barkat  Jan                    PF    19 0  28"+"\n"
    line[20]="BSITF0M010 Yasir Ubaid	                 ITC    18 20 31"+"\n"
    line[21]="BSITF0M010 Yasir Ubaid                   PF     25 21 34"+"\n"
    f.seek(0)
    f.writelines(line)
    f.seek(0)
    f.readline()
    f.readline()
    for line in f:
        rNo=line[:10]
        if len(rNo.strip())<10:
            print("Error in a file")
        mid=line[47:49]
        Ss=line[50:52]
        finals=line[53:55]
        if len(mid.strip())<1 or len(Ss.strip())<1 or  len(finals.strip())<1 :
            print("error in file")
    f.close()
    return
main()
