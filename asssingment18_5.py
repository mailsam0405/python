#retern addition of  numbers  of the numbers
import marvellousnum
def main():
      n=int(input("enter elemnts"))
      lst=[]
      sum=0

      for i in range(n):
          num=int(input("enter number"))
          lst.append(num)
          
      sum=0
      for i in lst:
           if marvellousnum.checkprime(i):
                sum=sum+i
          
      print(lst)
      print(sum)     
  

          
     
     
  
if __name__=="__main__":
     main()   