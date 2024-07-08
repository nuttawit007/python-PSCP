"""Week 3"""
def compare(num1, num2):
    """compare number"""
    if num1 > num2:
        return num1
    else:
        return num2

def main():
    """DataSpike"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    num6 = int(input())
    num7 = int(input())
    num8 = int(input())
    print(compare(compare(compare(compare(compare(compare(compare(num1, num2),\
         num3), num4), num5), num6), num7), num8))
main()
