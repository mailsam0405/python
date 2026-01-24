#lambda FUNCTION using filter () Returns odd of each  number
checkodd=lambda x: x%2!=0
def main():
  
    num=[int(x) for x in input("enter numbers:").split()]
    print(num)
    data=list(filter(checkodd,num))
    print(data)
   
  
    
   
   

if __name__=="__main__":
    main() 


