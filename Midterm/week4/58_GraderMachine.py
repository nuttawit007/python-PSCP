"""Week 4""" #***
def main(start, stop):
    """GraderMachine"""
    _pass, total = "", 0
    if start >= stop:
        for weight in range(start, stop-1, -1):
            if weight % 2 == 0:
                _pass += "%d "%weight
                total += weight
    else:
        for weight in range(start, stop+1):
            if weight % 2 == 0:
                _pass += "%d "%weight
                total += weight
    print("pass :", _pass)
    print("Sum :", total)
main(int(input()), int(input()))
