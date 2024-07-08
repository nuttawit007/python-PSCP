"""[Midterm 2023] Longer"""
import math
def longer(radius, width, lenght):
    """[Midterm 2023] Longer"""
    circle = math.pi*2*radius
    rectangle = (2*width) + (2*lenght)
    diff = abs(circle - rectangle)
    if circle > rectangle:
        print("Circle is longer")
        print("%.5f" % diff)
    elif rectangle > circle:
        print("Rectangle is longer")
        print("%.5f" % diff)
    else:
        print("Equal")
        print("%.5f" % diff)
longer(float(input()), float(input()), float(input()))
