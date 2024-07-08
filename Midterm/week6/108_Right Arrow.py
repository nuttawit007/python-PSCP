"""Week 6""" #***
def right_arrow(width, high):
    """Right Arrow"""
    gap = high//2
    for row in range(high):
        if row == 0 or row == high-1:
            print("*" * width)
        elif row > gap:#หลังจากบรรทัดกลาง
            print(" "*(gap-1) + "*"*width)
            gap -= 1
        else:#บรรทัดก่อนถึงบรรทัดกลาง
            print(" " * row + "*"*width)
right_arrow(int(input()), int(input()))

"""Right Arrow""" #ตะวัน
def arrow(width, height):
    """Draw Arrow"""
    for row in range(-height, height+1):
        print(' '*(height-abs(row)) + '*'* width)
arrow(int(input()), int(input())//2)