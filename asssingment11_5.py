#print the palindrome  
def main():
    no=(input("enter the number:"))
    if no==no[::-1]:
        print("yes")
    else:
        print("no") 
if __name__=="__main__":
    main()

