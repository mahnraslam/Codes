
# polymorphism 
class Animal:
    pass
class cat:
    def sound(cat):
        return "meow"    

class Dog:
  def sound(dog):
    return "bark"
cat1 = cat()    
dog1 = Dog()
print (cat1.sound())
print( dog1.sound())

# Encapsulation
class Person:
    pass
def set_name (person,name):
    person.name = name
    return f"name:{person.name},age:{person.age}, {person.gender}"


def set_age (person,age):
    if age > 0 and age < 100 :
        person.age = age
        return f"name:{person.name},age:{person.age}, {person.gender}"

    else :
        return "invalid age"

def set_gender (person, gender):
    if gender=="Male" or gender=="Female" or gender =="others":
        person.gender = gender
        return f"name:{person.name},age:{person.age}, {person.gender}"

    else :
        return "invalid"
        
per1 = Person()
per1.gender = "Male"
per1.name = "Daniyal"
per1.age = 17
per2 = Person()
per2.gender = "Female"
per2.name = "Noor"
per2.age = 19
per3 = Person()
per3.gender =  "Male"
per3.name = "Faiz"
per3.age = 20

print(set_age(per2,20))



'''
# inheritance
import math as m
class Shape:
    pass
     
def area():
        pass
    
class circle:
    pass
def area(c):
    return m.pi*c.radius*c.radius
    
c1 = circle()
c1.col = "red"
c1.radius = 3

c2 = circle()
c2.col = "green"
c2.radius= 4

class rectangle:
    pass
def area(r):
    return r.l*r.w

r1 = rectangle()
r1.col = "red"
r1.l = 3
r1.w  = 3


r2 = rectangle()
r2.col = "green"
r2.l = 4
r2.w = 3

print(area(r1))
'''


