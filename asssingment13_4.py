#print area of rectangle
def main():
  
    no=int(input("enter a number"))
    binary=""
    while no>0:
        binary=str(no%2)+binary
        no=no//2
    print("binary equvivalent=",binary)                 

if __name__=="__main__":
    main()

