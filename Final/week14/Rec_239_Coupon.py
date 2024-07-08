"""Week 14"""
def main(price):
    """Coupon"""
    pro1 = list(map(float, input().split()))
    pro2 = list(map(float, input().split()))
    coupon1, coupon2 = price, price
    if pro1[1] <= price:
        coupon1 = price - pro1[0]
    if pro2[1] <= price:
        coupon2 = price - (price*(pro2[0]/100))
    if price < pro1[1] and price < pro2[1]:
        print("Nope")
    elif coupon1 == coupon2 and pro1[1] == pro2[1]:
        print(1, "%.1f" % coupon1)
    elif coupon1 == coupon2:
        print("1 "+"%.1f" % coupon1 if pro1[1] < pro2[1] else "2 "+"%.1f" % coupon2)
    elif coupon1 < coupon2:
        print(1, "%.1f" % coupon1)
    elif coupon2 < coupon1:
        print(2, "%.1f" % coupon2)
main(float(input()))
