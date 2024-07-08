"""Blackjack"""
def blackjack(card):
    """Blackjack"""
    num = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
    stock = ""
    point = 0
    for _ in range(card):
        _type = input()
        stock += _type
        if _type == "K" or _type == "J" or _type == "Q":
            point += 10
        elif _type == "A":
            point += 11
        elif _type in num:
            point += int(_type)
    if point > 21 and stock.count("A") > 0:
        point -= 10
        if point > 21 and stock.count("A") > 1:
            point -= 10
    print(point)
blackjack(int(input()))
