def bubbleSort(a):
    i = 0
    while i < len(a):
        j = 0
        while j < (len(a)-1):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]
            j += 1
        i += 1
    return a
a = [67, 3, 2, 9, 2, 9, 88, 65, 38]
print(bubbleSort(a))




def SelectionSort(s,n):
    i=0
    while i < n-1:
        smallest = i
        j = i+1
        while j < n:
            if s[j] < s[smallest]:
                smallest = j
                s[i], s[j] = s[j], s[i]
            j += 1
        i+=1
    return s
a = [7,4,3,2,1]
print(SelectionSort(a,len(a)))


def reversebubbleSort(s,n):
    j = 0
    while j < (len(a)-1) :
        if a[j] < a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]
        j += 1
    return a
def main():
    a = [67, 3, 2, 9, 2, 9, 88, 65, 38]
    i=0
    z=len(a)
    n=i
    while i<len(a):
        s=reversebubbleSort(a[i],n)
        i+=1
    print(s)
main()



