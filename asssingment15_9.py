#lambda FUNCTION using filter () Returns count of even numbers 
no=lambda x:x%2==0 
def main():
  
    num=[int(x) for x in input("enter numbers:").split()]
    print(num)
    data=list(filter(no,num))
    print(data)
    print("count of even no:",len(data))
   
  
    
   
   

if __name__=="__main__":
    main() 


