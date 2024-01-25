def main(tuple):
    for i in range(len(tuple)):
        print(tuple[i])
tuple = ("mahnoor",0,5)
main(tuple)
import gc
class someObj :
    def __del__(self):
        print("obj is destroyed")
print(12)
obj = someObj()
print(22)
obj = someObj()
print(32)
obj = someObj()
n = gc.collect
print('garbadge',n)
