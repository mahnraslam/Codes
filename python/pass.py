class Grades:
    A = 4
    B = 3
    C = 2
    D = 2.5
def getValue(subject):
    if subject == "A":
        return Grades.A
    if subject == "B":
        return Grades.B
    if subject == "C":
        return Grades.B
    if subject == "D":
        return Grades.B
def calculateGPA(Pf,ICT,ICTLAB,ISL,Eng):
    gpa = (Pf + ICT + ICTLAB + ISL + Eng)/5
    return gpa
def main():
    a=input("Enter the grades of Pf")
    Pf = getValue(a)
    b=input("Enter the grades of ict")
    ICT = getValue(b)
    c=input("Enter the grades of lab")
    ICTLAB = getValue(c)
    d=input("Enter the grades of ISL")
    ISL = getValue(d)
    e=input("Enter the grades of Pf")
    ENG = getValue(e)

    print(calculateGPA(Pf,ICT,ICTLAB,ISL,ENG))
main()




