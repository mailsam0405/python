import threading


s = 0
p = 1

def sum_list(lst):
    global s
    s = sum(lst)

def product_list(lst):
    global p
    for i in lst:
        p *= i


lst = list(map(int, input("Enter numbers: ").split()))


t1 = threading.Thread(target=sum_list, args=(lst,))
t2 = threading.Thread(target=product_list, args=(lst,))


t1.start()
t2.start()


t1.join()
t2.join()


print("Sum of list:", s)
print("Product of list:", p)

if __name__ == "__main__":
    pass
