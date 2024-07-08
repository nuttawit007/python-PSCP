"""Week 3"""
def main(point_x, point_y):
    """Quadrant"""
    if point_x == 0 and point_y == 0:
        print("O")
    elif point_x > 0 and point_y > 0:
        print("Q1")
    elif point_x < 0 and point_y > 0:
        print("Q2")
    elif point_x < 0 and point_y < 0:
        print("Q3")
    elif point_x > 0 and point_y < 0:
        print("Q4")
    elif point_x == 0 and point_y != 0:
        print("Y")
    elif point_x != 0 and point_y == 0:
        print("X")
main(int(input()), int(input()))
