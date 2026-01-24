#lambda FUNCTION using filter () Returns list of numbers  which is divisible by 3and 5
no=lambda x:x%3==0 and x%5==0 
def main():
  
    num=[int(x) for x in input("enter numbers:").split()]
    print(num)
    data=list(filter(no,num))
    print(data)
   
  
    
   
   

if __name__=="__main__":
    main() 


