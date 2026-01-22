#print the factorial 
def main():
    no=int(input("enter the number:"))
    factorial=1
    for i in range(1, no+1):
        factorial *= i
    print(factorial)
if __name__=="__main__":
    main()

