#lambda FUNCTION using filter () Returns even  of each  number
checkeven=lambda x: x%2==0
def main():
  
    num=[int(x) for x in input("enter numbers:").split()]
    print(num)
    data=list(filter(checkeven,num))
    print(data)
   
  
    
   
   

if __name__=="__main__":
    main() 


