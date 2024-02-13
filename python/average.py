from random import randint
def SmesterWiseaverage(a,pro):
    print("for program",pro,end=" ")
    smsum=[0]*8
    for j in range (1,8):
        print("smester wise average of smester",j)
        for k in range(6):
            for l in range(10):
                smsum[j] += a[j][k][l]

    i=0
    while i<8:
        print("for smester:",i,smsum[i]//6//10)
        i+=1
    print()
def programWiseaverage(a,pro,smester,sub,stu):
    prosum=[0]*4
    for  i  in range(pro):
        for j in range (smester):
            for k in range(sub):
                for l in range(stu):
                    prosum[i] += a[i][j][k][l]
    for n in range (4):
        print("for  program",n,"avg:",prosum[n]//8//6//10)
    print()
def subjectWise(a,program,smester):
    sum=[0]*6
    print("for ,program",program,"smester:",smester)
    for k in range(6):
        for l in range(10):
                sum[k] += a[k][l]

    for n in range (6):
        print("avg:",sum[n]//10)
    print()
def computeResult(a,pro,smester):
    sum=0
    sumGPA=0
    for i in range(1):
        print("for program",pro,end="\t")
        for j in range(1):
            print ("for smester",smester)
            for k in range(6):
                for l in range(1):
                    sum +=a[i][j][k][l]
                    sumGPA +=(a[i][j][k][l]//25)*2
    print("Total marks",sum)
    print("percentage",sum//6)
    print("GPA",round((sumGPA/12),4))
    print()
def main():
    a=[[[[randint(66,100) for j in range(10)]for k in range(6)]for i in range(8)]for m in range(4)]
    programWiseaverage(a,4,8,6,10)
    computeResult(a,"DS",2)
    b=[[randint(33,99) for j in range(10)]for k in range(6)]
    s=subjectWise(b,"CS",1)
    return s
main()
