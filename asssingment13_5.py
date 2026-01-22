#print area of rectangle
def main():
  
    no=int(input("enter a marks"))
    if no>=75:
        print("distinction")
    elif no>=60:
        print("first class")
    elif no>=50:
        print("second class")
    else:
        print("fail")            
                   

if __name__=="__main__":
    main()

