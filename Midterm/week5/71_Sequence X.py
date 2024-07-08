"""Week 5""" #***
def main(num):
    """Sequence X"""
    for row in range(1, num+1):
        for col in range(num - row):
            print("  ", end=" ")
        for col in range(1, row+1):
            print("%02d" % col, end=" ")
        for col in range(row-1, 0, -1):
            print("%02d" % col, end=" ")
        print()
    for row in range(1, num):
        for col in range(row):
            print("  ", end=" ")
        for col in range(1, num+1-row):
            print("%02d" % col, end=" ")
        for col in range(num-(row+1), 0, -1):
            print("%02d" % col, end=" ")
        print()
main(int(input()))
