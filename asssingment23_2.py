class bankaccount():

    Rit=10.5

    def __init__(self,name,amount):
        self.AName=name
        self.AAmount=amount

    def display(self):
        print("ACCOUNT HOLDER:",self.AName,"CURRENT BALANCE:",self.AAmount)
    
    def diposit(self,amt):
        self.AAmount+=amt
        print("diposited:",amt)

    def withdraw(self,amt):
          if amt<=self.AAmount:
              self.AAmount-=amt    
              print("withdraw ammount:",amt)
          else:
              print("insufficient balance") 

    def calculateintrest(self):
        intrest=(self.AAmount*bankaccount.Rit)/100
        return intrest
        
    
obj1=bankaccount("samruddhi",10000)
obj1.display()
obj1.diposit(200)
obj1.withdraw(300)
print("intrest:",obj1.calculateintrest())



    
        
    
