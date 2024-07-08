"""Week 15"""
def main(year, mortor):
    """Tax"""
    reduce_tax = {6 : 0.1, 7 : 0.2, 8 : 0.3, 9 : 0.4}
    payment = 0
    if mortor > 1800:
        payment += (600*0.5) + (1200*1.5) + ((mortor-1800)*4)
    elif 601 <= mortor <= 1800:
        payment += (600*0.5) + ((mortor-600)*1.5)
    else:
        payment += ((mortor)*0.5)
    if 6 <= year <= 9:
        payment = payment - (payment*reduce_tax[year])
    elif year >= 10:
        payment = payment - (payment*0.5)
    print("%.2f" % payment)
main(int(input()), int(input()))
