from functools import reduce

number = lambda no: 70 <= no <= 90     # filter
increase = lambda no: no + 10          # map
product = lambda a, b: a * b           # reduce

def main():
    data = list(map(int, input("Enter numbers: ").split()))
    print("data:", data)

    fdata = list(filter(number, data))
    print("data after filter is:", fdata)

    mdata = list(map(increase, fdata))
    print("data after map is:", mdata)

    rdata = reduce(product, mdata, 1)   
    print("data after reduce is:", rdata)

if __name__ == "__main__":
    main()
