import threading

def main():
    pass

counter=0
lock=threading.Lock()

def incriment():
    global counter
    for i in range(100):
        lock.acquire()
        counter+=1
        lock.release()

t1 = threading.Thread(target=incriment)
t2 = threading.Thread(target=incriment)

t1.start()
t1.join()

t2.start()
t2.join()
print("final counter value:",counter)
if __name__ == "__main__":
    main()
