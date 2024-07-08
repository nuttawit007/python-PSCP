"""Week 6"""
def parallel(text):
    """Parallelogram"""
    # top left
    for row in range(1, len(text)+1):
        for col in range(len(text)-row):
            print(" ", end="")
        for col in range(row):
            print(text[col], end="")
        print()
    # btm right
    for row in range(1, len(text)):
        for col in range(row, len(text)):
            print(text[col], end="")
        print()
parallel(input())
