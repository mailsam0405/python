#check the number is divisible bye 3,5
def main():
    no=int(input("enetr a number:"))
    
    if (no%3==0) and (no%5==0):
        print("it is divisible")
    else:
        print("it is not divisible")    

     
    
if __name__=="__main__":
    main()

