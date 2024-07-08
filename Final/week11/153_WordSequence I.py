"""Week11"""
def main():
    """WordSequence I"""
    text = input()
    for row in range(1, len(text)+1):
        for col in range(row):
            print(text[col], end="")
        print()
main()
