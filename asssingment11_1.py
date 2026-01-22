#print the prime  number
def main():
    no=int(input("enter the number:"))
    for i in range(2,no):
            if no%i==0:
                print(no,"number is not prime")
                break
    else:
                print(no,"number is priem")
            

    
    

 
   
            
    
if __name__=="__main__":
    main()

