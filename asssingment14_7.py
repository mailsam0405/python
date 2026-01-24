#lambda FUNCTION of number it is divisible 5 if it is true otherwise false
def main():
    
     a=lambda x:True if x%5==0 else False
     no=int(input("enter a number:"))
     
     print(a(no))

if __name__=="__main__":
    main() 


