"""EuclideanDistance2D"""
import math
def main(var_q1, var_q2, var_p1, var_p2):
    """EuclideanDistance2D"""
    distance = math.sqrt(((var_q1 - var_p1)**2) + ((var_q2 - var_p2)**2))
    print(distance)
main(float(input()), float(input()), float(input()), float(input()))
