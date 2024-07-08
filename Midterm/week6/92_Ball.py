"""Week 6"""
def ball(heigh):
    """Ball"""
    last_high, _count = heigh*(3/5), 0
    while True:
        if last_high < 0.01:
            break
        last_high = last_high*(3/5)
        _count += 1
    print(_count)
ball(float(input()))
