"""Week 6"""
def check(num, condi):
    """เรียง: มาก-น้อย น้อย-มาก"""
    num1, num2, num3, num4 = int(num[0]), int(num[1]), int(num[2]), int(num[3])
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2, = num2, num1
    if condi == "ascend":
        return int(str(num1)+str(num2)+str(num3)+str(num4))
    elif condi == "descend":
        return int(str(num4)+str(num3)+str(num2)+str(num1))

def main(number):
    """Kaprekars"""
    _count, new_number = 0, number
    while new_number != "6174":
        new_number = str(check(new_number, "descend") - check(new_number, "ascend"))
        _count += 1
        if len(new_number) != 4:
            new_number += "0"*len(new_number)
    print(_count)
main(input())
