#print the prime  number
def main():
    sum=0
    no=int(input("enter the number:"))
    while no > 0:
        sum+=no%10
        no//=10
    print("sum of digits:",sum)     

   
if __name__=="__main__":
    main()

