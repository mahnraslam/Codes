def  solution(tokens):
    stack = []
    for n in tokens:                    # If the token is an operator, perform the corresponding operation
        if n == '+':
            stack.append(stack.pop() + stack.pop())
        elif n == '-':
            x, y = stack.pop(), stack.pop()
            stack.append(y - x)
        elif n == '*':
            stack.append(stack.pop() * stack.pop())
        elif n == '/':
            x, y = stack.pop(), stack.pop()         # Perform integer division and append the result to the stack
            stack.append(int(y / x))
        else:                                           # If the token is an operand, convert it to an integer and append to the stack
            stack.append(int(n))

        # The final result is the only element left in the stack
        return stack[-1]

tokens =  ["2","1","+","3","*"]
print(solution(tokens))

def raiseErrorCode(a,b):
    if b==0:
        raise Exception("denominator is zero")
    else:
        return a/b
print(raiseErrorCode(4,2))

def compLenStringEncode(string,k):
    check = string[0]
    c = 1
    s= ""
    i = 1
    while  i<len(string):
        if  string[i]==check :
            c =c+1

        else:
            if c > k:
                s = s + check +str(c)
                c = 1
                check = string[i]
            elif c==k:
                s = s + check
                c = 1
                check = string[i]
            else:
                c = 1
                check = string[i]
        i+=1
    if c > k:
        s = s +check +str(c)
    elif c==k:
        s = s +check

    return  len(s)

print(compLenStringEncode("aaabbaa", 3))


