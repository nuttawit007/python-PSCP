"""Week 6""" #***
def check(_round):
    """RuleofThree"""
    low_case, low_price, low_weight = 0, 0, 0
    for _ in range(_round):
        price = float(input())
        weight = float(input())
        total_price = price/weight
        if total_price < low_case or low_case == 0:
            low_price = price
            low_weight = weight
            low_case = total_price
        #กรณีคุ้มเท่ากัน แต่ใส่ราคามากว่าเข้าไปก่อน
        elif total_price == low_case and low_price > price: 
            low_price = price
            low_weight = weight
    print("%.2f %.2f" % (low_price, low_weight))
check(int(input()))
