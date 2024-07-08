"""Week 12"""
def main(coin1):
    """CoinChangev1"""
    coin25 = coin1//25
    coin1 = coin1%25
    coin10 = coin1//10
    coin1 = coin1%10
    coin5 = coin1//5
    coin1 = coin1%5
    print(coin25 + coin10 + coin5 + coin1)
main(int(input()))
