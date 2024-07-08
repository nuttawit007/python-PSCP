"""Week 5"""
def main(num):
    """Sequence III"""
    for row in range(num):
        for col in range(row+2, num+row+2):
            print(col, end=" ")
        print()
main(int(input()))
