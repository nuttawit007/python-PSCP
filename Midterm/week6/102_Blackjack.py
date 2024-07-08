"""Week 6"""
def blackjack(amount):
    """Blackjack"""
    score, stock = 0, ""
    for _ in range(amount):
        card = input()
        stock += card
        if card == "K" or card == "Q" or card == "J":
            score += 10
        elif card == "A":
            score += 11
        elif card.isdecimal():
            score += int(card)
    if stock.count("A") > 0 and score > 21:
        score -= 10
        if stock.count("A") > 1 and score > 21:
            score -= 10
    print(score)
blackjack(int(input()))
