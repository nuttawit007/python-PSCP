"""Week 5"""
def main(num): # 2
    """Sequence XI"""
    for row in range(-num + 1, num, 1): # range(-1, 2, 1) >> -1 0 1 
        for col in range(-num + 1, num, 1): #range(-1, 2, -1) >> -1 0 1
            """ 
            # 1 > 1-1 , 1 > 0-1 , 1 > 1-1
            # 0 > 1-1 , 0 > 0-1 , 0 > 1-1
            # 1 > 1-1 , 1 > 0-1 , 1 > 1-1
            """
            if abs(row) > abs(col) - 1:
                print("%02d" %(num - abs(row)), end=" ")
            else:
                print("%02d" %(num - abs(col)), end=" ")
        print()
main(int(input()))


def box():
    """Make Box"""
    center = int(input())
    for row in range(-1*center+1, center):
        for col in range(-1*center+1, center):
            print("%02d" % (center - max(abs(row), abs(col))), end=" ")
        print()
box()