#print the factorial number
def main():
    factorial=1
    a=int(input("enetr the number:"))
    for i in range(1,a+1):
        factorial=factorial*i
    print("factorial is:",factorial)    
            
    
if __name__=="__main__":
    main()

