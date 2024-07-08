"""Final 03"""
def floor_one(area):
    """50 - 150 floor"""
    if 100 <= area <= 150:
        return 5000
    elif 151 <= area <= 250:
        return 6000
    elif 251 <= area <= 300:
        return 7000
    elif 301 <= area <= 350:
        return 8000
    elif 351 <= area <= 400:
        return 9000
    elif 401 <= area <= 450:
        return 10000
    elif 451 <= area <= 550:
        return 12000

def floor_two(area):
    """150 - 500 floor"""
    if 551 <= area <= 700:
        return 14000
    elif 701 <= area <= 1000:
        return 18000
    elif 1001 <= area <= 1200:
        return 21000
    elif 1201 <= area <= 1400:
        return 23000
    elif 1401 <= area <= 1500:
        return 24000
    elif 1501 <= area <= 2000:
        return 30000
    elif 2001 <= area <= 2500:
        return 34000

def main(area, high, people, hot, outdoor):
    """BTU"""
    btu = 0
    if area <= 550:
        btu += floor_one(area)
    else:
        btu += floor_two(area)
    if high > 8:
        btu += (high-8)*1000
    if people > 2:
        btu += (people-2)*600
    if hot == "kitchen":
        btu += 4000
    if outdoor == "facing the sun":
        btu += btu*0.1
    if outdoor == "shaded":
        btu -= btu*0.1
    print(int(btu))
main(int(input()), int(input()), int(input()), input(), input())



# การทำช่วงของข้อมูลโดยใช้ range
"""BTU"""
def btu(size, heigh, people, heat, sun):
    """btu"""
    ans = 5000*(size in range(100, 151)) + 6000*(size in range(151, 251))\
+ 7000*(size in range(251, 301)) + 8000*(size in range(301, 351))\
+ 9000*(size in range(351, 401)) + 10000*(size in range(401, 451))\
+ 12000*(size in range(451, 551)) + 14000*(size in range(551, 701))\
+ 18000*(size in range(701, 1001))\
+ 21000*(size in range(1001, 1201)) + 23000*(size in range(1201, 1401))\
+ 24000*(size in range(1401, 1501))\
+ 30000*(size in range(1501, 2001)) + 34000*(size in range(2001, 2501))
    ans += (max(heigh-8, 0)*1000) + (max(people-2, 0)*600) +\
        (4000*(heat == 'kitchen'))
    ans = (ans*(110/100))*(sun == 'facing the sun') + (ans*(90/100))*(sun == 'shaded')\
    + ans*(sun == 'Normal')
    print(int(ans))
btu(int(input()), int(input()), int(input()), input(), input())