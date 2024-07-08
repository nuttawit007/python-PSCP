"""Week 3"""
def main(pointx_me, pointy_me, radius, mosquito_x, mosquito_y):
    """Circular I"""
    circle = (((mosquito_x - pointx_me)**2) + ((mosquito_y - pointy_me)**2))**(0.5)
    if circle <= radius:
        print("Yes")
    else:
        print("No")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
