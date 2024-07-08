"""Math for IT"""
import math
def main(radius):
    """Math for IT"""
    area = math.pi*(radius**2)
    circum = 2*math.pi*radius
    print("Area: %.3f" % area)
    print("Circumference: %.3f" % circum)
main(float(input()))
