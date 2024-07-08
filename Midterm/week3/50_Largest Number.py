"""Week 3"""
def high(num1, num2):
    """compare max"""
    if num1 > num2:
        return num1
    else:
        return num2

def main(num1, num2, num3):
    """Largest Number"""
    style1 = int(num1+num2+num3)
    style2 = int(num1+num3+num2)
    style3 = int(num2+num1+num3)
    style4 = int(num2+num3+num1)
    style5 = int(num3+num1+num2)
    style6 = int(num3+num2+num1)
    print(high(high(high(high(high(style1, style2), style3), style4), style5), style6))
main(input(), input(), input())
