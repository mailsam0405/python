#addtion of all numbers
def add():
     n=int(input("enter elemnts"))
     lst=[]
     sum=0

     for i in range(n):
          num=int(input("enter number"))
          lst.append(num)
          sum=sum+num
     print(lst)
     print(sum)     
  

          
  
if __name__=="__main__":
     add()   