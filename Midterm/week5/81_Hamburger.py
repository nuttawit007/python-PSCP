"""Week 5"""
def main(left, right):
    """Hamberger"""
    print("|"*left + "*"*((left+right)*2) + "|"*right)
main(int(input()), int(input()))
