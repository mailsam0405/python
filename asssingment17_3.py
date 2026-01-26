#print factorial of number 
def fun():
   
   fact=1
   n=int(input("enter no")) 
   for i in range(1,n+1):
       fact= fact*i
   print(fact)


if __name__=="__main__":
    fun()   