class demo():
    value=0

    def __init__(self,a,b):
        self.no1=a
        self.no2=b

     

    def fun(self):
        print("no1:",self.no1)
        print("no2:",self.no2)

    def gun(self):
        print("no1:",self.no1)
        print("no2:",self.no2)


obj1=demo(11,21)
obj2=demo(51,101)        

#call instance method
obj1.fun()
obj2.fun()
obj1.gun()
obj2.gun()