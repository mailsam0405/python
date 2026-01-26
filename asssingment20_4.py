import threading

def main():
    pass

def small(s):
    count = 0
    for ch in s:
        if ch.islower():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread name:", threading.current_thread().name)
    print("Lowercase characters:", count)

def capital(s):
    count = 0
    for ch in s:
        if ch.isupper():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread name:", threading.current_thread().name)
    print("Uppercase characters:", count)

def digits(s):
    count = 0
    for ch in s:
        if ch.isdigit():
            count += 1
    print("Thread ID:", threading.get_ident())
    print("Thread name:", threading.current_thread().name)
    print("Digits:", count)    


s = input("Enter a string: ") 


t1 = threading.Thread(target=small, args=(s,), name="small")
t2 = threading.Thread(target=capital, args=(s,), name="capital")
t3 = threading.Thread(target=digits, args=(s,), name="digits")


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()

if __name__ == "__main__":
    main()
