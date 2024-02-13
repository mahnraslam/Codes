class Fruit:
    def __init__(self , name, uprice, uname,sucount, suname):
        self.__name = name
        self.__uprice = uprice
        self.__unitName = uname
        self.__countInSale = sucount
        self.__saleUnitName = suname

    def __repr__(self):
        return f"{self.__name} and price:{str(self.__uprice)} per {self.__unitName} saleable as {self.__saleUnitName}, {str(self.__countInSale)}"
    def __str__(self):
        return f"{self.__name} price:{str(self.__uprice)} per {self.__unitName} saleable as {self.__saleUnitName}, {str(self.__countInSale)}"

    def setName(self, d):
        self.__name = d
        return
    def getName(self):
        return self.__name

    def setUnitPrice(self, d):
        self.__uprice = d
        return
    def getUnitPrice(self):
        return self.__uprice

    def setUnitName(self, d):
        self.__uname = d
        return
    def getUnitName(self):
        return self.__uname

    def setcountInSale(self, d):
        self.__countInSale = d
        return
    def getcountInSale(self):
        return self.__countInSale

    def setsaleUnitName(self, d):
        self.__saleUnitName = d
        return
    def getsaleUnitName(self , d):
        return self.__saleUnitName


    def compare(self,other):
        r = ""
        if self ==other:
            r = "Both are same"
        else:
            r = "Both are different"
        return r

    staticmethod(compare)
def main():
    k = Fruit("kela",30 , "unit", 12,"dozen")
    j = Fruit("Apple",35 , "kg", 1,"kg")
    m = Fruit("Pears",30 , "kg", 1,"kg")
    n = Fruit("Orange",35 , "unit", 12,"dozen")
    z = Fruit("kela",34 , "unit", 12,"dozen")
    print(Fruit.compare(k,n))
    print(Fruit.compare(k,j))
    print(Fruit.compare(k,j))
    print(Fruit.compare(k,k))
    print(Fruit.compare(k,m))
main()



