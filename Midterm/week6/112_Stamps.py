"""Week 6"""
def main(timetoeat, billtostamp, stampup, sasomtopro, pro):
    """Stamps"""
    mystamp, mybill = 0, 0
    for _ in range(timetoeat):
        price = int(input())
        if mystamp >= sasomtopro:
            #rounddis lod ki rob
            rounddis = price // pro
            if price % pro > 0:
                rounddis += 1
            tmp = mystamp // sasomtopro
            can = min(rounddis, tmp)
            if can > 0:
                price -= can * pro
                price = max(price, 0)
                mystamp -= can * sasomtopro
        if price >= billtostamp:
            mystamp += (price//billtostamp)*stampup
        mybill += price
    print(mybill)
    print(mystamp)
main(int(input()), int(input()), int(input()), int(input()), int(input()))
