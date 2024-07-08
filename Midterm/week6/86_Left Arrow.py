"""Week 6"""
def left_arrow(width, length):
    """Left Arrow"""
    gap = length//2
    for _ in range(length):
        print(" "*abs(gap-_)+"*"*width)
left_arrow(int(input()), int(input()))
