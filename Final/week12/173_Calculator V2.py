"""Week 12"""
def main(num, total):
    """Calculator"""
    if num == 1:
        total = 1
    else:
        for i in range(len(str(num))):
            if i == len(str(num))-1:
                total += (num-(10**i)) * ((len(str(num)))+1)
            else:
                total += (9 * (10**i)) * (len(str(10**i))+1)
        total += len(str(num)) + 1
    print(total)
main(int(input()), 0)
