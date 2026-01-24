#lambda FUNCTION Returns maximum of number
def main():
    
     a=lambda x,y:x if x>y else y
     x=int(input("enter a number:"))
     y=int(input("enter a number:"))
     

     print("the no is maximum:",a(x,y))
  
  

if __name__=="__main__":
    main() 


