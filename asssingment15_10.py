#lambda FUNCTION using reduce () Returns the product of all  number
from functools import reduce
no=lambda x,z: x*z
def main():
  
    num=[int(x) for x in input("enter numbers:").split()]
    print(num)
    data=(reduce(no,num))
    print(data)
   
  
    
   
   

if __name__=="__main__":
    main() 


