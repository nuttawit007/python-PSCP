"""CompositeFunction"""
def funf(xoi):
    """equationf"""
    return 2*xoi

def fung(xoi):
    """equationg"""
    return (xoi/2)+1

def main(xoi):
    """main"""
    print("%.2f" % funf(fung(xoi)))
    print("%.2f" % fung(funf(xoi)))
main(int(input()))
