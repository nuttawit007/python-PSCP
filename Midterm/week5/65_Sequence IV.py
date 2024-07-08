"""Week 5"""
def main(num):
    """Sequence IV"""
    for row in range(num):
        for col in range(1+(row*num), num+1+(num*row)):
            print(col, end=" ")
        print()
main(int(input()))
