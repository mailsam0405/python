#lambda FUNCTION Returns even of number print if it is true otherwise false
def main():
    
     a=lambda x:True if x%2==0 else False
     no=int(input("enter a number:"))
     
     print(a(no))

if __name__=="__main__":
    main() 


