import threading
def main():
   pass
def even(n):
    total = 0
    print("even factors:")
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            print(i)
            total += i
    print("sum of even factors:", total)

def odd(n):
    total = 0
    print("odd factors:")
    for i in range(1, n+1):
        if n % i == 0 and i % 2 != 0:
            print(i)
            total += i
    print("sum of odd factors:", total)

num = int(input("enter number: "))

t1 = threading.Thread(target=even, args=(num,))
t2 = threading.Thread(target=odd, args=(num,))

t1.start()
t1.join()

t2.start()
t2.join()

print("exit from main")
if __name__=="_main__":
    main()
