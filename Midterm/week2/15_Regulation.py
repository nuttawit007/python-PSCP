"""Regulation"""
def main(num, flo, txt):
    """Regulation"""
    print("%30d" % num)
    print("%030d" % num)
    print("%.2f" % flo)
    print("%.12f" % flo)
    print("%40s" % txt)
main(int(input()), float(input()), str(input()))
