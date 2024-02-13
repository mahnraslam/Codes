import pandas as pd
import numpy as np
import array
#2D array
data = [["sara","hira","noor"],[12,23,45]]
data = pd.DataFrame(data)
#print(data)
#numerical
arr = np.array([[1,2,3],[4,5,6] ])
data = pd.DataFrame(arr,index =[ "A","B"] ,columns =["a","b","c"])
print(data)

#{[],[],[]}
data ={"name":["sara","hira","noor"],"age":[12,23,45]}
data = pd.DataFrame(data)
#print(data)

#key becomes coloum headings
#2D dictionary
data = {"student1":{"name":"Mahnoor","CLass":"BS","Age":19},"student2":
    {"name":"Sara","CLass":"BS","Age":19},"student3" : {"name":"Insha","Degree":"BS","Age":19}}
data = pd.DataFrame(data)
print()

#[{},{}]
#Dictionary within lists
student1 = {"name":"Mahnoor","CLass":"BS","Age":19}
student2 = {"name":"Sara","Degree":"BS","Age":19}
students = [student1,student2,]
data = pd.DataFrame(students)
#print(data)
#Specify coloumn index
data = [ {"name":"Mahnoor","CLass":"BS","Age":19},{"name":"Sara","CLass":"BS","Age":19}]
data = pd.DataFrame(data, index=["student1","student2"])
print()
#Series
#{"staff":Series(1),"salary" :series2}
a ={1:2,2:4,3:9}
z = pd.Series(a)
a ={1:2,2:4,3:9}
y = pd.Series(a)
#print(z)
#print(z.values)
data =[y,z]
data =pd.DataFrame (data)
#print(data)

#From another D.F
