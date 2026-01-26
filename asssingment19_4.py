#fmr
from functools import reduce
checkeven=lambda no: no %2==0   #filter
    
square=lambda no:no*no #map


add=lambda a,b:a+b #reduce

def main():
    data = list(map(int, input("Enter numbers: ").split()))
    print("data:", data)
    
   

    fdata=list(filter(checkeven,data))
    print("data after filter is:",fdata)

    mdata=list(map(square,fdata))
    print("data after map is:",mdata)

    rdata=reduce(add,mdata)
    print("data after reduce is:",rdata)
 
if __name__=="__main__":
     main()
