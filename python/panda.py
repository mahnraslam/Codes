# while loop for float
#But for loop does'nt provide this facility
import pandas as pd
a =  [1,2,3,4]
b = [1,2,3,4]
d = pd.Series(b)
c = pd.Series(a)
print(d+c)
c = pd.Series(a , index =["A","B","c","d"])
d = pd.Series(b)
#print(c+d)                                                         #value error when index are less
print("End")
#series one col datasheet group of series
#TUPLE
f = (1,3,5,5,6)

#Dictionery
a ={1:2,2:4,3:9}
z = pd.Series(a)
a ={1:2,2:4,3:9}
y = pd.Series(a)
print(z)
print(z.values)
data =[y,z]
data =pd.DataFrame (data)
print(data)

# ans in numpy ..values
#both are attributes
z = [24,5,6,43,4,"sara"]
z = pd.Series(f,index=["a","b","c","d","e"])

#other way
#z = pd.Series(range(5))
#print(z)


z = [1,2,3,None,None]
y = [2,3,4,1,2]
z = pd.Series(z)
y  = pd.Series(y)
print(y>2)


print(z.dtypes)
print(z.shape)          #ans in tuple (5,) cols..tuple#well for rows and cols #a =(2) int
print(z.nbytes)
print(z.ndim)
print(z.size)
print(z.empty)
print(z.tail(2))
print(z.head(2))
#FUNCTIONS
print(z.count())
print( z.sort_values())
#print(y+z)
# NAN for empty values #hasnans attribute


