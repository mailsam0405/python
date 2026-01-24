#lambda FUNCTION using reduce () Returns maximum number
from functools import reduce
minimum=lambda x,z: x if x<z else z
def main():
  
    num=[int(x) for x in input("enter numbers:").split()]
    print(num)
    data=(reduce(minimum,num))
    print(data)
   
  
    
   
   

if __name__=="__main__":
    main() 


