"""Week 11"""
def one_zero(num):
    """find 1/0"""
    if num%2 == 0:
        return "0"
    else:
        return "1"

def main(ten_bit):
    """Binary"""
    new_ten, two_bit = ten_bit, ""
    if ten_bit == 0:
        two_bit += "0"
    while new_ten != 0:
        two_bit += one_zero(new_ten)
        new_ten //= 2
    print(two_bit[::-1])
main(int(input()))

'''Binary''' #ภูมิ
def to_2(num, current=""):
    '''Binary'''
    if not num:
        print(current or "0")
        return
    elif num%2: # if remain
        current = "1" + current
        to_2(num//2, current)
    else:
        current = "0" + current
        to_2(num//2, current)
to_2(int(input()))