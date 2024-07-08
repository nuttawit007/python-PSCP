"""Week 6"""
def main(price_first, define_min, voucher_percent, offer):
    """Restaurant"""
    pricesum = price_first+offer
    if pricesum >= define_min:
        pricesum = pricesum*voucher_percent
    if price_first >= define_min:
        price_first = price_first*voucher_percent
    if price_first < pricesum:
        print("No %.3f" % (pricesum-price_first))
    elif price_first > pricesum:
        print("Yes %.3f" % (price_first-pricesum))
    else:
        print("Yes")
main(float(input()), float(input()), (100-float(input()))/100, float(input()))
