"""Week 5"""
def main(num):
    """Sequence I"""
    for _ in range(num):
        for col in range(1, num+1):
            print(col, end=" ")
        print()
main(int(input()))
