"""Week4""" #***
def main():
    """SumOfNumber"""
    sumwant = int(input())
    sumval = 0
    while True:
        inputnum = int(input())
        if inputnum == -1:
            break
        sumval += inputnum
        if sumval == sumwant:
            break
    print(sumval)
main()
