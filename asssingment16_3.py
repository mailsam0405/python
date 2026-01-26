#add

def add(no1,no2):
    return no1+no2

def main():
    value1=0
    value2=0
    ret=False

    value1=int(input("enetr first number:"))
    value2=int(input("enetr second number:"))
    ret=add(value1,value2)
    print("additionm of numbers is:",ret)

    
    
    
if __name__=="__main__":
    main()    