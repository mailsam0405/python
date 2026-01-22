#print area of rectangle
def main():
    length=int(input("enter a length"))
    width=int(input("enter a width"))
    area=(lambda length,width:length*width)(length,width)
    print(area)
   
   
if __name__=="__main__":
    main()

