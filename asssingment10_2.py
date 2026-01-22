#print the sum of n natural number
def main():
    a=int(input("enetr the number:"))
    sum=0
    for i in range(1,a+1):
        sum=sum+i
    print("the sum of first",a,"natural number is:",sum)         
    
if __name__=="__main__":
    main()

