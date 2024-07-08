"""Week 6""" #*** ยากทรงได้ฟรีแล้วเอาฝาที่ฟรีไปแลกฟรีอีก
def main(price, pro, changemilk, money):
    """Milk"""
    milk = money // price
    tmp = milk
    while tmp >= pro and changemilk != 0:
        if pro == 0:
            break
        milk += changemilk
        tmp += changemilk
        tmp -= pro
    print(milk)
main(int(input()), int(input()), int(input()), int(input()))

"""milk"""
def milk(price, lid, free, money):
    """milk(ไม่รู้วิธีคิดถูกมั้ย อาจจะดูงงๆ แต่คำตอบออกมาได้ เพราะ "bruteforce")"""
    bottle = money//price #หาจำนวนราคาต่อขวด
    summation = bottle #กำหนดค่าเพื่อลูปหาค่าที่ต้องการ เน้นย้ำว่าตอนแรกได้ขวดเท่านี้
    while bottle >= lid and lid != 0: #เงื่อนไขที่โจทย์บอก
        get_bottle = bottle // lid #หาจำนวนขวดโดยการเอาราคาที่ได้มาหารด้วยจำนวนฝาขวดเพื่อแลกนมขวด
        get_bottle = get_bottle*free #จำนวนขวดที่แลกได้
        summation = summation + get_bottle #จำนวนขวดทั้งหมดที่ได้ในตอนนี้
        bottle = bottle - (bottle//lid) * lid  #รวมกับขวดที่ได้รับฟรีเพิ่มเติม
        bottle = bottle + get_bottle #จำนวนขวดสูงสุดที่เราได้
    print(summation) #ข้อนี้คิดเลขแจ่มๆ
milk(int(input()), int(input()), int(input()), int(input()))
