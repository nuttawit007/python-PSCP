"""Week 6"""
def turn():
    """Turnstile"""
    stock = ""
    while True:
        text = input().upper()
        if text == "END":
            break
        else:
            stock += text
    print(stock.count("CP"))
turn()
