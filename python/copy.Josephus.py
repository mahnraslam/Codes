import copy
def freedom(a,n, start):
    k= start - 1
    for i in range(len(a)):
        for j in range(n):
            if k+1==len(a) :
                k=0
            else:
                k=k+1
        a.remove(a[k])
        k=k-1

        if len(a)==1:
            print(a)
            break

a=["A","B","C","D","E","F","G"]
print(freedom(a,3, 4))

def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1
n = 7  # Number of people in the circle
k = 3  # Every third person is eliminated
survivor = josephus(n, k)
print("The survivor is at position:", survivor)

#Shallow Copy
#Deep Copy
#b=a.copy()
#b=list(a)
#b=a[:]
list2 = [3,5,3]
list1=[[2,3,4],[2,3,6],[6,7,8]]
copylist1 =copy.copy(list1)

deepcopylist1 = copy.deepcopy(list1)
list1[1][2] =[1,6,7,8]
#Copy and deepcopy behave in the same way in 1D

print(copylist1)
print(deepcopylist1)
#Sets
#Alias means no copy
'''
def justafunction(lst):
    lst[0]=999
    lst.append(777)
    print(id(lst))


def main():
    data = [2,4,9,7,3]
    print(data)

    cpdata = data
    cpdata.pop(4)
    print(data)

    justafunction(data)
    print(data)

    print(id(data))
    print(id(cpdata))

main()
'''
def min_len_after_deletion(s, k):
    count = 1
    result = len(s)

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_len = len(str(count)) if count > 1 else 0
            result -= min(count, k) - encoded_len
            count = 1
    encoded_len = len(str(count)) if count > 1 else 0
    result -= min(count, k) - encoded_len

    return result

s = "aabbaa"
k = 2
result = min_len_after_deletion(s, k)
print(result)
