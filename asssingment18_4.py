#return frequancy  of the numbers
def main():
     
     n=int(input("enter elemnts"))
     lst=[]
     
     for i in range(n):
          num=int(input("enter number"))
          lst.append(num)
       

     search=int(input("enter elements to search"))
    
     print(lst.count(search))
               
  
if __name__=="__main__":
     main()   