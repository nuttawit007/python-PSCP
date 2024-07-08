"""Week 3"""
def main(condi, int_a, int_b, int_c):
    """sort"""
    if int_a > int_b:
        int_a, int_b = int_b, int_a
    if int_b > int_c:
        int_b, int_c = int_c, int_b
    if int_a > int_b:
        int_a, int_b = int_b, int_a
    if condi == "Ascend":
        print("%.2f, %.2f, %.2f" % (int_a, int_b, int_c))
    elif condi == "Descend":
        print("%.2f, %.2f, %.2f" % (int_c, int_b, int_a))
main(input(), float(input()), float(input()), float(input()))
