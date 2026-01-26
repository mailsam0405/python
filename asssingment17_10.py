#print  addition of numbers 
def add():
     num=int(input("enter number:"))
     total=0
     for i in range(num):
          total=total+(num%10)
          num=num//10
          if num==0:
            break
     

     print(total)     
     
   

    
       
  
if __name__=="__main__":
     add()   