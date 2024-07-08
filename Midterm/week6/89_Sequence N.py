"""Week 6"""
def seqn(num):
    """Sequence N"""
    for row in range(1, num+1):
        for col in range(1, num+1):
            if col == 1 or col == num or row == col:
                print("*", end="")
            else:
                print(" ", end="")
        print()
seqn(int(input()))
