#fmr
from functools import reduce
def checkprime(no):  #filter
    if no<2:
         return False
    for i in range(2,no):
            if no%i==0: 
                 return False
            else:
                 return True

def multiply(no): #map
    return no*2

def maximum(a,b): #reduce
    return a if a>b else b

def main():
    data = list(map(int, input("Enter numbers: ").split()))
    print("data:", data)
    
    fdata=list(filter(checkprime,data))
    print("data after filter is:",fdata)

    mdata=list(map(multiply,fdata))
    print("data after map is:",mdata)

    rdata=reduce(maximum,mdata)
    print("data after reduce is:",rdata)
 
if __name__=="__main__":
     main()
