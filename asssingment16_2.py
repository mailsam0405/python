#chekeven

def ChkNum(no):
    if no%2==0:
        return("even number")
    else:
        return("odd number")


def main():
    value=0
    ret=False

    print("enetr number")
    value=int(input())
    ret=ChkNum(value)
    print(ret)

    
    
    
if __name__=="__main__":
    main()    