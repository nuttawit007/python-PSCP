"""TheFunctionWithin"""
def funf(aaa):
    """functionF"""
    return 2*aaa

def fung(aaa):
    """functionG"""
    return (3*(aaa**4))-(aaa**3)+(2*(aaa**2))+10

def funh(aaa, bbb, ccc):
    """functionH"""
    return ((ccc+aaa)**2)-(aaa*bbb)+(bbb**2)

def funi(aaa, bbb, ccc, ddd):
    """functionI"""
    return ((aaa**2)+(bbb**2)-(ccc**2))/((ddd**2)-(2*aaa*ddd)+(2*aaa))

def main(aaa, bbb, ccc, ddd):
    """TheFunctionWithin"""
    print(funf(funf(aaa)))
    print(fung(funf(aaa-bbb)))
    print(funh(funf(aaa+bbb), funf(aaa+ccc), fung(funf(ddd**2))))
    print(funi(funh(funf(aaa+bbb), funf(aaa-ccc), fung(funf(ddd**2))),\
     fung(funf(aaa-bbb)), funf(funf(funf(funf(funf(ccc))))), ddd**8))
main(float(input()), float(input()), float(input()), float(input()))
