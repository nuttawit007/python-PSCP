"""Hmaberger"""
def hamberger(left, right):
    """bread and meat"""
    for _ in range(left):
        print("|", end="")
    for _ in range((left + right)*2):
        print("*", end="")
    for _ in range(right):
        print("|", end="")
hamberger(int(input()), int(input()))

# วิธีเทพ
def hamberger(left,right):
    print(left*"|" + (left*right)*"*" + right*"|")
hamberger(int(input()), int(input()))