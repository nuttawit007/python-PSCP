"""Week 7"""
def main(bit, parity, num1):
    """[Midterm 2022] Parity"""
    for num in bit:
        if num == "1":
            num1 += 1
    if parity == "Even":
        if num1 % 2 == 0:
            bit += "0"
        else:
            bit += "1"
    elif parity == "Odd":
        if num1 % 2 == 0:
            bit += "1"
        else:
            bit += "0"
    print(bit)
main(input(), input(), 0)
