#retern addition of  numbers  of the numbers
def checkprime(num):
            
            if num<2:
                  return False
            for i in range(2,num):
                  if num%i==0:
                        return False
            else:
                  return True      
                         
     
  
if __name__=="__main__":
     checkprime()   