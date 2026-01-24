#lambda FUNCTION Returns largest  of number
def main():
     a=lambda x,y,z:x if x>y and x>z else(y if y>z else z) 
     x=int(input("enter a number:"))
     y=int(input("enter a number:"))
     z=int(input("enter a number:"))
      
     
     print("the largest number ",a(x,y,z))
  
  
    
  
   

if __name__=="__main__":
    main() 


