"""Week 3"""
def main():
    """FoodGrade I"""
    weight_chicken = list(map(lambda _: int(input()), range(24))) #map() >> ใช้รับ input 24 ค่าแล้วแปลงเป็น int
    filter_chicken = list(filter(lambda x: 50 <= x <= 70, weight_chicken)) #filter() >> กรองค่า 50-70
    print(len(filter_chicken))
main()

