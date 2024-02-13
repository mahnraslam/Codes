from random import randint
def print3D(a,years,dep,cft):
    for i in range(years):
        print(f"for year 202{i}")
        print()
        for j in range(dep):
            print(f"for department {j+1}")
            for k in range(cft):
                print(a[i][j][k],end="  ")
            print()

def  departmentWise(a,yearIndex, totalDept, totalCert ):

    maximum=[0]*4
    for j in range(totalDept):
        maximum[j]=a[4][j][0]
        for k in range(5):
            if a[4][j][k]>maximum[j]:
                maximum[j]=a[4][j][k]

        print("for department ",j+1," maximum is",maximum[j])
def yearWiseMinOfITDeptWebCertificate(array, totalYears , itDeptIndex, webCertIndex):
    for i in range(totalYears):
        min=array[i][itDeptIndex][webCertIndex]
        print(f"for year 200{i} min is {min}")


def main():
    a=[[[randint(14,99)for k in range(5)]for j in range(4)]for i in range(6)]
    print3D(a,6,4,5)
    departmentWise(a,6,4,5)
    yearWiseMinOfITDeptWebCertificate( a, 6, 1 , 3 )

main()








