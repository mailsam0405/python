class arithmatic():
    def __init__(self):
        self.value1=0
        self.value2=0

    def accept(self):
        self.value1=int(input("enter number:"))    
        self.value2=int(input("enter number:"))    

    def addition(self):
        return self.value1+self.value2

    def substraction(self):
         return self.value1-self.value2     

    def multiplication(self):
         return self.value1*self.value2  

    def divison(self):
         return self.value1/self.value2      


obj1=arithmatic()
obj1.accept()
print("addition:",obj1.addition()) 
print("substraction:",obj1.substraction())  
print("multiplication:",obj1.multiplication())  
print("divison:",obj1.divison())       