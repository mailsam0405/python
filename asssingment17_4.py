#print  addition factors of number 
def main():
  n=int(input("enter number"))
  sum=0
  for i in range(1,n//2+1):
     if n%i==0:
        sum+=i
  print(sum)        


if __name__=="__main__":
    main()   