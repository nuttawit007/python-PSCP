"""Week 5""" #***
def main(num):
    """Sequence VI"""
    for row in range(num):
        for col in range(1, row+2):
            print(col, end=" ")
        print()
main(int(input()))
