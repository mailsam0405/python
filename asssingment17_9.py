#print numbers of digits
def counts():
     count=0
     no=int(input("enter the number"))
     for i in range(no):
          count+=1
          no=no//10
          if no==0:
               break
     print(count)        
  
if __name__=="__main__":
     counts()   