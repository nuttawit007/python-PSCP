"""Week10"""
def main():
    """MissingNumber"""
    num = int(input())
    lis_num = []
    while True:
        digit = int(input())
        if digit == 0:
            break
        lis_num.append(digit)
    no_num = [i for i in range(1, num+1) if i not in lis_num]
    for item in no_num:
        print(item)
main()
