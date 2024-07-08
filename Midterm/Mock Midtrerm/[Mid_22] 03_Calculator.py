"""Week 7"""
def main(num, stock):
    """[Midterm 2022] Calculator"""
    if num == "1":
        print(1)
    else:
        for digit in range(1, int(num)+1):
            stock += len(str(digit))
        print(stock + int(num))
main(input(), 0)
