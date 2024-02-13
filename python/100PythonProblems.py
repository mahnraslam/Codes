import random
# Water  "gun"
def waterGame():
    choices = ["snake","water","gun"]
    i = 0
    User_points = 0
    computer_points = 0
    while i < 5:
        lst = random.choice (choices)
        user = input("enter water, snake or  gun: ")
        if user== "snake" :
            if lst== "gun":
                computer_points += 1
            elif lst=="water":
                User_points += 1
        elif user== "water":
            if lst== "snake":
                computer_points += 1
            elif lst=="gun":
                User_points += 1
        elif user== "gun":
            if lst== "snake":
                computer_points += 1
            elif lst=="water":
                User_points +=1
        else:
            print("invalid selection")
        i += 1
    if User_points > computer_points:
        print("you are winner")
    elif User_points<computer_points:
        print("you had lost this game ")
waterGame()


#ArmstronNumber
def armstrongNumber(num):
    power = len(str(num))
    length = power
    sum = 0
    for i in range(length):
        value = num % 10
        sum += value**length
        num //= 10
    print(sum)
    '''
    sum = 0
    for i in range(length):
        value = num //10**(power-1)
        sum += value**length
        num = num %10**(power-1)
        power -=1
    print(sum)'''
armstrongNumber(1634)

x = 0
y = 1
z = 0

for i in range(12):
    pass
    #print(z)
    x= y
    y = z
    z = x+y


test_str = "GeeksforGeeks"


all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print("Count of all characters in GeeksforGeeks is :\n "
      + str(all_freq))


