#return maximum of the numbers
def main():
     n=int(input("enter elemnts"))
     
     lst=[]
    

     for i in range(n):
          num=int(input("enter number"))
          lst.append(num)

     print("list",list)
     print("maximum number:",max(lst))

          
  
if __name__=="__main__":
     main()   