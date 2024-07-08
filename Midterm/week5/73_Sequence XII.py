"""Week 5"""
def main(num):
    """Sequence XII"""
    for row in range(-num + 1, num, 1):
        for col in range(-num + 1, num, 1):
            print("%02d" %(num - abs(abs(row)-abs(col))), end=" ")
        print()
main(int(input()))
