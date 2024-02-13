word = "PythonCode"
print(word[2:8:-2])  #nothing will print if not a stop value nothing will print
print("/\\")
print(len({"name":"sara","age":32,"name":"hira"}))
a = [1,2,3,4]
b = [ 3 ,4 ,6 ]
c = [2 , 3 ,4]
print([tuple(a),tuple(b),tuple(c)])

num =list(zip(a,b,c))
print(num)




print(12,"like twelve")
a=3
b=4
c=5
quardaticEQ=lambda x:a*x**2+b*x+c
print(quardaticEQ(-3))
#instead of mannulay using append fuction you should use map function
my_list=[1,2,3,8,9]
new_list=list(map(lambda x:x*2 ,my_list))
print(new_list)
new_list=list(filter(lambda x:x>2 ,my_list))
print(new_list)

#Tuple
a=(1,3,4,5,6,7,8)
#lambda x:3*x+1
g = lambda x: 3*x+1
print(g(3))
g= lambda x:((x**2)*(x**2))-(x*x)**2
print(g(3))
h= lambda x,y,z:(x+y-z)
print(h(3,2,1))
a=["Amna fiaz","sara","nadia","hira","maha"]
a.sort(key=lambda name:name.split()[-1].lower())
print(a)






'''while True:
    n=int(input("enter 8 to exit"))
    if n!=8:
        def add(a,b):
            print(a+b)
        def subtract(a,b):
            print(a-b)
        def main():
            a=int(input("enter:"))
            b=int(input("enter:"))
            n=int(input("enter 1 for a and 2 for sub or 8 to exit"))
            if n==1:
                add(a,b)
            elif n==2:
                subtract(a,b)
        main()
    else:
        break'''

