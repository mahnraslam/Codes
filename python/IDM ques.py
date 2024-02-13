name = "abc"
c="c"
if c in name:
    print(1)
def devide(a,b):
    try:
        print(a/b)
    except:
        print("dominator is zero")
    else:
        print("succesfully run")
    finally:
        print()
devide(12,3)


a = [1.2,3,4]
b = [2,34,4]

#Functions of the list :Pop,extend,insert,remove,sort,array.index("element"),reverse,discard,index
#del(inventory["ProductNo1_releaseYear"])
#del(inventory["ProductNo2_releaseYear"])
print(dict)
print(a+b)
a.append(b)
print(a)

set1 = {"a","d",2}
set2 = {2}
set2.add(3)                                                             #we use add not append
person = {"sara":"manager","noor":"ceo"}
items = list(person.items())
print(items)
print(set2.issubset(set1))
print(set1 & set2)
'''
a=["sara","Saba","Saad","Saman","Sidra","sara"]
b=[1,2,3]
a.insert(2,b)
b=tuple(a)
print(b.index("Saba"))

a.pop(2)        #remove from specific index use in just list
print(a)
print(a.index("Saba"))
print(a.count("sara"))
print(a[1:4:2])
b={1,23,3,4,5,6}                #sort,index ,count are not attributes in set
c=set(a)                      #Auto sort int when convert into list,however manually write sort with str

#SET
print({'sara','Saba'}.issubset(c))
print(c.issupe
rset({'Saad','Saba'}))




a={1,2,34,5,3,5,"Nadia"}
#a[5]="Nadia" List assignment is not possible
a.add(2)
a.remove(34)
a.discard(5)
print(a)
b={11,12,13,14,15}
print(a.union(b))
'''

stu1={"name":"Mahnoor","Roll No":"BSDSF23A037","id":1213}
print(stu1["name"])
try:
   print(stu1["cityName"])
except:
    print("This post does'nt have location")
loc = stu1.get("cityName",None)
print(loc)
for key in stu1.keys():
    value=stu1[key]
    print(key,end=" ")
    print(value)
for k,value in enumerate(stu1):
    print(k,value)
