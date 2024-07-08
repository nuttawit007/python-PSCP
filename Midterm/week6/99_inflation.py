"""Week 6""" #***
def inflation(money, year):
    """Inflation"""
    money = int(money*100) #กรณีค่าที่เข้าครั้งแรก ทศนิยมเกิน 2 ตน
    for _ in range(year):
        infla = (money*381)//10000 #ทำเป็นหลักหมื่น
        money = money + infla
    print("%d.%02d" % (money//100, money%100)) #แยกเอา 2 ตัวท้ายของหลักหมื่นเป็น ทศนิยม 2 ตน
inflation(float(input()), int(input()))
