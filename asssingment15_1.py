#lambda FUNCTION using map () Returns square   of each  number
def main():
 
    num=list(map(int,input("enter numbers:").split()))
    data=list(map(lambda x: x*x,num))
    print(data)
   
  
    
  
   

if __name__=="__main__":
    main() 


