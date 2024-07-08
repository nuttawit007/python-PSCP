"""Week 7"""
import math
def main(var_a, var_b, var_c):
    """[Midterm 2022] Heron of Alexandria"""
    var_s = (var_a+var_b+var_c)/2
    area = math.sqrt(var_s*(var_s-var_a)*(var_s-var_b)*(var_s-var_c))
    print("%.3f" % area)
main(float(input()), float(input()), float(input()))
