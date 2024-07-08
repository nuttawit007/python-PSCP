"""final 07"""
def main():
    """Water"""
    month = int(input())
    var_a = float(input())
    var_b, var_c = float(input()), float(input())
    var_d = float(input())
    total = 0
    for _ in range(month):
        num = float(input())
        pay = 0
        if num > var_b:
            pay += (var_a*var_b) + ((num-var_b)*var_c)
        else:
            pay += num*var_a
        if pay <= var_d:
            pay = 0
        total += pay
    print("%.2f" % total)
main()
