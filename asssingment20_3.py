import threading

def main():
    pass

def evenlist(lst):
    evens = []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
    print("Even elements:", evens)
    print("Sum of even elements:", sum(evens))

def oddlist(lst):
    odds = []
    for i in lst:
        if i % 2 != 0:
            odds.append(i)
    print("Odd elements:", odds)
    print("Sum of odd elements:", sum(odds))


num = list(map(int, input("Enter list elements: ").split()))


t1 = threading.Thread(target=evenlist, args=(num,))
t2 = threading.Thread(target=oddlist, args=(num,))


t1.start()
t2.start()

t1.join()
t2.join()

if __name__ == "__main__":
    main()
