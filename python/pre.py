a = 2
b = 8
i = a*b
while i>0:
    if i%a==0 and i%b==0:
        lcm =i
    i-=1
print(lcm)
my_list=[1,2,3,8,9]
new_list = list(map(lambda x:x*2 ,my_list))
print(new_list)
new_list=list(filter(lambda x:x%2==0 ,my_list))
print(new_list)

size = 10
r = 1
while r <= size:
    c = size
    while c >= size - r:
        print(" ", end="")
        c = c - 1
    while c >= 1:
        print("@", end="")
        c = c - 1
    print()
    r = r + 1
size = 8
r = 1
while r <= size:
    c = 1
    while c <= r**2:
        pass
        #print("@", end="")
        c = c + 1
    #print()
    r = r + 1



f=open('number','rb')
z = f.read(16)
print(int.from_bytes(z,byteorder='big'))
f.close()



def display(current_value):
    print(f"Current Value: {current_value}")
    return current_value

def add(current_value, operand):
    result = current_value + operand
    display(result)
    return result, [current_value]

def subtract(current_value, operand):
    result = current_value - operand
    display(result)
    return result, [current_value]

def multiply(current_value, operand):
    result = current_value * operand
    display(result)
    return result, [current_value]

def divide(current_value, operand):
    if operand != 0:
        result = current_value / operand
        display(result)
        return result, [current_value]
    else:
        print("Error: Division by zero")
        return current_value, []
def power(current_value, exponent):
    result = current_value ** exponent
    display(result)
    return result, [current_value]

def remainder(current_value, divisor):
    if divisor != 0:
        result = current_value % divisor
        display(result)
        return result, [current_value]
    else:
        print("Error: Division by zero")
        return current_value, []

def reset():
    display(0)
    return 0, []

def undo(current_value, previous_values):
    if previous_values:
        previous_value = previous_values[-1]
        display(previous_value)
        return current_value,previous_values[:-1]
    else:
        print("Error: Cannot undo further")
        return current_value, previous_values


def run_calculator():
    current_value = 0
    previous_values = []

    # Initial display
    display(current_value)

    while True:
        command = input("Enter command (+, -, , /, *, %, end, reset, undo): ").lower()

        if command == 'end':
            print("Calculator program ended.")
        elif command == 'reset':
            current_value, previous_values = reset()
        elif command == 'undo':
            previous_values = undo(current_value, previous_values)
        else:
            try:
                operand = float(input("Enter operand: "))
                if command == '+':
                    current_value, previous_values = add(current_value, operand)
                elif command == '-':
                    current_value, previous_values = subtract(current_value, operand)
                elif command == '*':
                    current_value, previous_values = multiply(current_value, operand)
                elif command == '/':
                    current_value, previous_values = divide(current_value, operand)
                elif command == '**':
                    current_value, previous_values = power(current_value, operand)
                elif command == '%':
                    current_value, previous_values = remainder(current_value, operand)
                else:
                    print("Invalid command. Please enter a valid operator.")
            except ValueError:
                print("Invalid operand. Please enter a valid number.")

run_calculator()

