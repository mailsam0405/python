import threading

def main():
    pass

def maximum(lst):
    print("Maximum element:", max(lst))

def minimum(lst):
    print("Minimum element:", min(lst))


lst = list(map(int, input("Enter elements: ").split()))        

t1 = threading.Thread(target=maximum, args=(lst,))
t2 = threading.Thread(target=minimum, args=(lst,))

t1.start()
t1.join()

t2.start()
t2.join()
 
if __name__ == "__main__":
    main()
