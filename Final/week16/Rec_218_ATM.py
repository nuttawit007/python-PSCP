"""week 16"""
def main(money):
    """ATM"""
    while True:
        tran = input()
        if tran == "END":
            break
        tran = tran.split()
        if tran[0] == "D":
            money += int(tran[1])
        elif tran[0] == "W":
            money -= int(tran[1])
        if money < 0:
            money = 0
    print(money)
main(int(input()))
