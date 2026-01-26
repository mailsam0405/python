import threading

def prime(lst):
    print("prime numbers:")
    for n in lst:
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    break
                else:
                    print(n)

def nonprime(lst):
    print("prime non-numbers:")
    for n in lst:
        if n<=1:
            print(n)
        else:
            for i in range(2,n):
                if n%i==0:
                    print(n)                    
                    break
    
                    
lst=list(map(int,input("enter numbers:").split()))


t1 = threading.Thread(target=prime, args=(lst,))
t2 = threading.Thread(target=nonprime, args=(lst,))


t1.start()
t2.start()


t1.join()
t2.join()



if __name__ == "__main__":
    pass
