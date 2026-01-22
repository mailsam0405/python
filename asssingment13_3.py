#print area of rectangle
def main():
    sum=0
    no=int(input("enter a number"))
    for i in range(1,no):
        if no%i==0:
            sum=sum+i
    if sum==no:
        print("it is perfect number")
    else:
        ("it is not perfect number")           

if __name__=="__main__":
    main()

