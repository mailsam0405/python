#print prime number 
def fun():
    no=int(input("enter number"))
    for i in range(2,no):
        if  no%i==0:
            print("it is not prime number")
            break
    else:
             print("it is  prime number")    

   
   


if __name__=="__main__":
    fun()   