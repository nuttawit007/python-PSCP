"""Week 3"""
def main(var_a, var_b, var_c):
    """sort"""
    if var_c**2-0.01 <= var_a**2 + var_b**2 <= var_c**2+0.01:
        print("Yes")
    elif var_b**2-0.01 <= var_a**2 + var_c**2 <= var_b**2+0.01:
        print("Yes")
    elif var_a**2-0.01 <= var_b**2 + var_c**2 <= var_a**2+0.01:
        print("Yes")
    else:
        print("No")
main(float(input()), float(input()), float(input()))
