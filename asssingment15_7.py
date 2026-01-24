#lambda FUNCTION using filter () Returns list of string  having length greter than 5
length=lambda x :len(x)>5
def main():
  
    num=input("enter string:").split()
    print(num)
    data=list(filter(length,num))
    print(data)
   
  
    
   
   

if __name__=="__main__":
    main() 


