"""Week 3"""
def main(center_x, center_y, radius, point_x, point_y):
    """Point in Circle"""
    circle = ((point_x - center_x)**2) + ((point_y - center_y)**2)
    if circle <= radius ** 2:
        print("True")
    else:
        print("False")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
