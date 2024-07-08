"""Backward"""
def main():
    """Backward"""
    stock = []
    while True:
        text = input()
        if text == "NULL":
            break
        stock.append(text)
    stock = stock[::-1]
    for item in stock:
        print(item)
main()
