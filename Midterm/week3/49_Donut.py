"""Week 3"""
import math
def main(price, buy, free, donut):
    """Donut"""
    pay, get_donut = 0, 0
    if price > 0 and buy > 0 and free >= 0 and donut >= 0:
        buy_free = buy+free
        if donut%buy_free >= buy or donut%buy_free == 0:
            pay += buy*price*(math.ceil(donut/buy_free))
            get_donut += buy_free*(math.ceil(donut/buy_free))
            donut -= buy_free*(math.ceil(donut/buy_free))
        elif donut%buy_free < buy:
            pay += buy*price*(math.ceil(donut/buy_free)-1)
            get_donut += buy_free*(math.ceil(donut/buy_free)-1)
            donut -= buy_free*(math.ceil(donut/buy_free)-1)
        if donut > 0:
            pay += donut * price
            get_donut += donut
        print(pay, get_donut)
    else:
        pay += price*donut
        get_donut = donut
        print(pay, get_donut)
main(int(input()), int(input()), int(input()), int(input()))


def main(price,buy,free,want): #จารโช # 2 4 3 12 >> 16 14
    """Donut"""
    box = buy+free # 4 + 3 = 7 >> 1 กล่องมีกี่ชิ้น
    price_per_box = price*buy # 2 * 4 = 8 >> ราคาต่อกล่อง
    numbox = want//box # 12 // 7 = 1 >> กี่กล่องดี
    remain = want - (numbox*box) # 12-(1*7) = 5 >> เหลือกี่ชิ้น

     # เหลือเยอะกว่า promotion ถ้าเหลือน้อยกว่าซื้อเป็นชิ้นๆจะดีกว่า
    if remain >= buy: # 5 >= 4
        numbox = numbox+1  # numbox = 1+1 = 2
        remain = 0
    price = (numbox*price_per_box)+(remain*price) #(2*8)+(0*2) = 16
    piece = numbox*box+remain # 2*7+0 = 14
    print(price, piece) # 16 14
main(int(input()), int(input()), int(input()), int(input()))
