"""Week 3"""
def main(number):
    """Seven"""
    remainder = number%4
    if remainder == 1:
        print(7)
    elif remainder == 2:
        print(9)
    elif remainder == 3:
        print(3)
    elif remainder == 4:
        print(1)
main(int(input()))
