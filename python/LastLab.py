f=open('number','rb+')
d=1024
#f.write(int.to_bytes(d,16, 'big'))
#print(f.read())
z = f.read(4)
j = int.from_bytes(z,byteorder="little")
print(j)
f.close()

'''f=open("photo.bmp","rb+")
f.seek(22)
z=f.read(4)
j = int.from_bytes(z,byteorder="little")
print(j)
m = j//4
f.seek(22)
c = m.to_bytes(4,byteorder="little")
f.write(c)
f.close()'''
def main():
    f=open("File.txt","r+")
    while True:
        n=int(input("which function you want to perform: for read:1 , for changing line:2 ,for del: 3,5 for edit:5 ,press"))
        if n==1:
            b=f.read()
            print(b)
        if n==2:
            lines = f.readlines()
            line_number = int(input("Enter the line number to modify: "))
            new_content = input("Enter the new content: ")
            lines[line_number - 1] = new_content + '\n'
            f.seek(0)
            f.writelines(lines)
            print(f"Line {line_number} mo modified successfully.")


        if n==3:
            i=int(input("which record you want to del"))
            lines=f.readlines()
            lines[i-1]=(" "*56) +"\n"
            print(f"Line {i} del successfully.")
            f.seek(0)
            f.writelines(lines)
        if n == 5:
            line_number = int(input("enter line number::"))
            response = input("which portion u wannna to change in this line:")
            lines = f.readlines()
            try :
                if response =="name":
                    name = input("enter changing name:")
                    contents = lines[line_number-1]
                    rollNumber = contents[:10 ]
                    lines [line_number-1] = rollNumber + name +" "*(30-len(name)) +contents[40:56] +"\n"
                    print("name changed")

                elif response =="Roll Number":
                    rollNumber = input("enter roll number")
                    contents = lines[line_number-1]
                    lines[line_number-1] = rollNumber + contents[11:57]+"\n"
                    print("roll  number is modified")
            except:
                print("only write word in this form: name,Roll Number")

            f.seek(0)
            f.writelines(lines)
        if n==4:
            break
    f.close()
main()

'''file_path = 'File.txt'
with open(file_path, 'r+') as file:
    lines = file.readlines()
    line_number = int(input("Enter the line number to modify: "))
    new_content = input("Enter the new content: ")
    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = new_content + '\n'
        file.seek(0)
        file.writelines(lines)
        print(f"Line {line_number} mo modified successfully.")
    else:
        print(f"Invalid line number: {line_number}")
file.close()'''


'''f= open("File.txt","r+")
file = open("mistakes","w")
f.readline()
f.readline()
error = 0
z=3
for line in f:
    content=line.split()
    if len(content [0]) < 10:
        error += 1
        print(content[0])
        print("Roll num error:",content[0])
        file.write(line+"\n")
    if  len(content[2]) < 2:
        error += 1
        file.write(line+"\n")

    if  len(content[3]) < 2:
        error += 1
        file.write(line+"\n")
        print("marks error",content[3])
    if  len(content[4]) < 2:
        error += 1
        file.write(line+"\n")
print(error)
file.close()
f.close()'''








