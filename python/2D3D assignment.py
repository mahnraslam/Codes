class coin:
    cent = 1
    dime = 10
    quarter = 25
    dollar = 100

def inputCoin():
    t = input()

    if t == "cent":
        return coin.cent
    if t == "dime":
        return coin.dime
    if t == "quarter":
        return coin.quarter
    if t == "dollar":
        return coin.dollar

def printCoin(c):
    if c == coin.cent:
        print("cent")
    if c == coin.dime:
        print("dime")
    if c == coin.quarter:
        print("quarter")
    if c == coin.dollar:
        print("dollar")

def main():

    print("Enter three coin names one by one")
    print("all different, two same, all same")
    c1 = inputCoin()
    c2 = inputCoin()
    c3 = inputCoin()

    print("Third coin you entered is")
    printCoin(c3)

main()
class DayTimes:
    Dawn=0
    Mor=1
    Noon=2
    night=3
def inputNum():
    n=input("enter the day times:")
    if n=="Dawm":
        return DayTimes.Dawn
    if n=="Mor":
        return DayTimes.Mor
    if n=="Noon":
        return DayTimes.Noon
    if n=="night":
        return  DayTimes.night

    return n
def output(a):

    if a==DayTimes.Dawn:
        print("THe day time is Dawn")
    if a==DayTimes.Mor:
        print("THe day time is Morning")
    if a==DayTimes.Noon:
        print("THe day time is Noon")
    if a==DayTimes.night:
        print("THe day time is night")

def main():
    c = inputNum()
    c1 = inputNum()
    c2 = inputNum()
    output(c)
    output(c2)
    output(c1)

main()


