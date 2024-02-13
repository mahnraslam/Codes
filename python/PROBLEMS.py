b ="school"
a =[1,2,3,4]
print(a[0:2])
print(b[0:2])
rand = random.random()*100
print(rand)
import ctypes
longint = ctypes.c_int
j = longint()
j = 9
print(j**3)

ArrayType = ctypes.py_object * 5
slots = ArrayType()

i = 0
slots[i] = 5-i
i += 1
slots[i] = 5- 2
i += 1
slots[i] = 5- 6
i += 1
slots[i] = 5-i
i += 1
slots[i] = 5-i


print(slots)
print(slots[4])


while True:
    n = int(input('enter num or 8 to exit'))
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(factorial)
    if n==8:
        break

name = input("Enter name: ")
z_count = 0
o_count = 0

if len(name) <= 20 and name[0] == "z" and name[-1] == "o":
    for char in name:
        if char == "z":
            z_count += 1
        elif char == "o":
            o_count += 1

    if z_count * 2 == o_count:
        print("Yes")
    else:
        print("No")
else:
    print("No")


def convertLenEncode(a):
    s = ""
    i = 0
    while i < len(a):
        for j in range(int(a[i+1])):
           print(a[i],end="")
        i += 2
    print(s)
convertLenEncode("n2c3j4")
numbers =[1,2,3,3,4]
#for i,number in enumerate(numbers):
    #print(i,number)

import matplotlib.pyplot as plt
class Circle:
    def __init__(self,colour,height,width):

        self.colour= colour
        self.height= height
        self.width = width
    def drawCircle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), height =self.height,width =self.width,fc=self.colour))
        plt.show()

c1 = Circle("red",1 ,1)
#print(c1.drawCircle())

# https://pythonexamples.org/python-pillow/
from PIL import Image

def newImg():
    img = Image.new('RGB', (30, 40))
    img.putpixel((25, 30), (255, 0, 0))
    img.rectangle((200, 125, 300, 200), fill=(255, 0, 0), outline=(0, 255, 0))
    #img.save(r'C:\Users\idrees\Desktop\sqr.png')

    return img

newImg().show()
newImg().resize((750, 900)).show()
newImg().rotate(45).show()

filename = "Idrees.jpg"
with Image.open(filename) as img:
    img.load()

print(type(img))

print(isinstance(img, Image.Image))

#img.show()
img.rotate(15).show()



'''

Python Imaging library

python -m pip install Pillow


https://realpython.com/image-processing-with-the-python-pillow-library/

'''





