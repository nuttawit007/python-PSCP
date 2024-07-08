"""Week 13"""
def main(money, percent, year):
    """Compound Interest"""
    total_money = money
    for _ in range(year):
        total_money = total_money + (total_money * (percent/100))
    print("%.2f" % total_money)
main(int(input()), float(input()), int(input()))
