class numbers():
                       
    def __init__(self,a):
        self.value=a

    def checkprime(self):
        if self.value<2:
            return False
        for i in range(2,self.value):
            if self.value%i==0:
                return False
            return True
        
    def checkfactors(self):
        for i in range(1,self.value+1):
            if self.value%i==0:
                print(i)    

    def checkperfect(self):
        sum=0
        for i in range(1,self.value):
            if self.value%i==0:
                sum=sum+i
        if sum==self.value:
            return True
        else:
            return False
        

obj1=numbers(10)
print("factors:",obj1.checkfactors)
print("prime:",obj1.checkprime)
print("perfect:",obj1.checkperfect)      
