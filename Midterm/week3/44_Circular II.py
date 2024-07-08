"""Week 3"""
import math
def main():
    """Circular II"""
    px_me = float(input())
    py_me = float(input())
    rad_me = float(input())
    px_you = float(input())
    py_you = float(input())
    rad_you = float(input())
    distance_2point = math.sqrt(((px_me-px_you)**2)+(py_me-py_you)**2)
    save_zone = rad_me + rad_you
    if distance_2point >= save_zone:
        print("No")
    else:
        print("Yes")
main()
