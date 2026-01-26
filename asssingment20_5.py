
import threading
def main():
    pass
def thread1():
    print("thread1 output:")
    for i in range(1,51):
        print(i)

def thread2():
    print("thread2 output:")
    for i in range(50,0,-1):
        print(i)        

t1=threading.Thread(target=thread1,name="thread1")
t2=threading.Thread(target=thread2,name="thread2")

t1.start()
t1.join()

t2.start()
t2.join()
 
if __name__=="__main__":
    main() 