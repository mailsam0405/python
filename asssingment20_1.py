#even ,odd
import threading
def main():
    pass
def even():
    print("first 10 even number:")
    for i in range(2,21,2):
        print(i)

def odd():
    print("first 10 odd number:")
    for i in range(1,20,2):
        print(i)        

t1=threading.Thread(target=even,name="even")
t2=threading.Thread(target=odd,name="odd")

t1.start()
t1.join()

t2.start()
t2.join()
 
if __name__=="__main__":
    main() 