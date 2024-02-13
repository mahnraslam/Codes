def main():
    f  = open("Grades.txt","r")
    file = open(" Report.txt","w")
    department=["BSE","BIT"]
    file.write("\t\t University of the Punjab"+"\n")
    file.write("\t\t College of information technology "+"\n")
    file.write("\t\t Result of session : Spring 2020 "+"\n")
    subjects=3
    stuOfSE=4
    stuOfIT=3
    f.readline()
    f.readline()
    for i in range ((len(department))):
        file.write("Degree:"+str(department[i])+"\n")
        file.write("SR.No  Roll No   Student Name                   ITC  PF DLD Total %age Grade"+"\n")
        file.write("===== ========== ============================== === === === ===== ==== ====="+'\n')
        if i==0:
            z=1
            sumSub1 = 0
            sumSub2 = 0
            sumSub3 = 0
            totalStuMarks=0
            for k in range(stuOfSE):
                sub=[0]*3
                totalSum = 0
                for j in range(subjects):
                    content = f.readline()
                    content = content.split()
                    SrNo = " 00"+str(z)+" "
                    rNo = content[0]
                    name = content[1]+" "+content[2]
                    if j==0:
                        file.write(str(SrNo)+rNo + "  "+name+"\t\t       ")

                    sub[j]=int(content[4])+int(content[5])+int(content[6])
                    file.write("  "+str(sub[j]) )
                    totalSum += sub[j]

                totalStuMarks += totalSum
                avg = totalSum/ 3
                avg=round(avg,1)
                if avg>=85 and avg<=99:
                    grade="A+"
                elif avg>=80 and avg<=85:
                    grade="A-"
                elif avg>=75 and avg<=80:
                    grade="B+"
                elif avg>=70 and avg<=74:
                    grade="B-"
                elif avg>=65 and avg<=69:
                    grade="C+"
                elif avg>=60 and avg<=64:
                    grade="C-"
                elif avg>=55  and avg<=59:
                    grade="D+"
                elif avg>=50 and avg<=54:
                    grade="D-"
                elif avg>=40 and avg<=49:
                    grade="E"
                elif avg>=0 and avg<=39:
                    grade="F"
                file.write("   "+str(totalSum)+" "+str(avg)+"  "+str(grade) )
                sumSub1 += sub[0]
                sumSub2 += sub[1]
                sumSub3 += sub[2]
                z+=1
                file.write("\n")

            avg1=round(sumSub1/stuOfSE)
            avg2=round(sumSub2/stuOfSE)
            avg3=round(sumSub3/stuOfSE)
            totalStuMarksAvg = totalStuMarks//stuOfSE

            file.write("\t\t\t\t\t\t=========================="+"\n")
            file.write("\t\t\t\tBSE Degree Avg: "+str(avg1)+"  "+str(avg2)+"   "+str(avg3)+"  "+str(totalStuMarksAvg))
            file.write("\n")
    if i==1:
            z=1
            sumSub1 = 0
            sumSub2 = 0
            sumSub3 = 0
            totalStuMarks=0
            for k in range(stuOfIT):
                sub=[0]*3
                totalSum = 0
                for j in range(subjects):
                    content = f.readline()
                    content = content.split()
                    SrNo = " 00" + str(z)+" "
                    rNo = content[0]
                    name = content[1]+" "+content[2]
                    if j==0:
                        spaces=30-len(name)
                        file.write(str(SrNo)+rNo + "  "+name+str(chr(32)*spaces))

                    sub[j]=int(content[4])+int(content[5])+int(content[6])
                    file.write("  "+str(sub[j]) )
                    totalSum += sub[j]

                totalStuMarks += totalSum
                avg = totalSum/ 3
                avg=round(avg,1)
                if avg>=85 and avg<=99:
                    grade="A+"
                elif avg>=80 and avg<=85:
                    grade="A-"
                elif avg>=75 and avg<=80:
                    grade="B+"
                elif avg>=70 and avg<=74:
                    grade="B-"
                elif avg>=65 and avg<=69:
                    grade="C+"
                elif avg>=60 and avg<=64:
                    grade="C-"
                elif avg>=55  and avg<=59:
                    grade="D+"
                elif avg>=50 and avg<=54:
                    grade="D-"
                elif avg>=40 and avg<=49:
                    grade="E"
                elif avg>=0 and avg<=39:
                    grade="F"
                file.write("   "+str(totalSum)+" "+str(avg)+"  "+str(grade) )
                sumSub1 += sub[0]
                sumSub2 += sub[1]
                sumSub3 += sub[2]
                z+=1
                file.write("\n")

            avg1=round(sumSub1/stuOfIT)
            avg2=round(sumSub2/stuOfIT)
            avg3=round(sumSub3/stuOfIT)
            totalStuMarksAvg = totalStuMarks//stuOfIT

            file.write("\t\t\t\t\t\t=========================="+"\n")
            file.write("\t\t\t\tBIT Degree Avg: "+str(avg1)+"  "+str(avg2)+"   "+str(avg3)+"  "+str(totalStuMarksAvg))

    file.close()
    f.close()
main()


