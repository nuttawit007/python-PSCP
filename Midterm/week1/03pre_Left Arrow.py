"""Left Arrow"""
def arrow(width, lenght): #loop patern
    """Left Arrow"""
    for row in range(1, lenght+1): #แถวกลาง
        if row == int((lenght+1)/2):
            print("*"*width)
        elif row < (lenght+1)/2: #แถวน้อยกว่าแถวกลาง
            print(" "*(int(((lenght+1)/2))-row) + "*"*width)
        elif row > (lenght+1)/2: #แถวมากกว่าแถวหลาง
            print(" "*(row-int(((lenght+1)/2))) + "*"*width)
arrow(int(input()), int(input()))

# วิธีเทพ
def arrow(width, lenght):
    gap = lenght//2
    for _ in range(lenght):
        print(" " * abs(gap - _) + "*" * width)
arrow(int(input()), int(input()))