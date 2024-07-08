"""Week 6"""
def elo(_ra, _rb, letter):
    """Elo"""
    if letter == "A":
        _ea = 1/(1+10**((_rb-_ra)/400))
        print("%.2f" % _ea)
    elif letter == "B":
        _eb = 1/(1+10**((_ra-_rb)/400))
        print("%.2f" % _eb)
elo(int(input()), int(input()), input())
