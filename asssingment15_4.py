#lambda FUNCTION using reduce () Returns addition  of all number
from functools import reduce
add=lambda x,z: x+z
def main():
  
    num=[int(x) for x in input("enter numbers:").split()]
    print(num)
    data=(reduce(add,num))
    print(data)
   
  
    
   
   

if __name__=="__main__":
    main() 


