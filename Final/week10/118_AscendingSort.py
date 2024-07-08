"""AscendingSort"""
def main():
    """AscendingSort"""
    stock = []
    for _ in range(5):
        num = int(input())
        stock.append(num)
    stock.sort()
    for item in stock:
        print(item)
main()
