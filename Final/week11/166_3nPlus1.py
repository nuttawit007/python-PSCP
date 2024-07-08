"""Week11"""
#ใช้ recursive แทน loop
def check_amount(num, count=1):
    """check mamount number"""
    if num == 1:
        return count
    elif num%2 == 0:
        count += 1
        return check_amount(num/2, count)
    else:
        count += 1
        return check_amount(num*3+1, count)

def main():
    """3nPlus1"""
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            print(check_amount(num))
main()
