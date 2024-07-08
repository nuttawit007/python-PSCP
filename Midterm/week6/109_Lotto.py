"""Week 6""" #***
def lotto():
    """Lotto"""
    fir_lot = input()
    last2_lot = input()
    front3_lot1, front3_lot2 = input(), input()
    last3_lot1, last3_lot2 = input(), input()
    mylotto = input()
    near_first1, near_first2 = "", ""
    if fir_lot == "000000":
        near_first1 = "000001"
        near_first2 = "999999"
    elif fir_lot == "999999":
        near_first1 = "000000"
        near_first2 = "999998"
    else:
        near_first1 = ("%06d" %(int(fir_lot)-1))
        near_first2 = ("%06d" %(int(fir_lot)+1))
    # แยกกรณี เผื่อได้เลขที่เหมือนกันเปะ เช่น ท้าย3ตัว 1:560 2:560
    total_prize = 0
    if fir_lot == mylotto:
        total_prize += 6000000
    if near_first1 == mylotto or near_first2 == mylotto:
        total_prize += 100000
    if mylotto[-2:] == last2_lot:
        total_prize += 2000
    if mylotto[:3] == front3_lot1:
        total_prize += 4000
    if mylotto[:3] == front3_lot2:
        total_prize += 4000
    if mylotto[-3:] == last3_lot1:
        total_prize += 4000
    if mylotto[-3:] == last3_lot2:
        total_prize += 4000
    print(total_prize)
lotto()
