"""Week 5"""
def key(num):
    """key"""
    sum_num1, sum_num2 = 0, 0
    #ผลรวม 13 หลัก
    for digit in num:
        sum_num1 += int(digit)
    #3 หลักสุดท้าย * 10
    sum_num2 += int(num[-3:])*10
    #con1 + con2
    total = str(sum_num1 + sum_num2)
    if len(total) > 4:
        print(total[-4:])
    elif int(total) < 1000:
        print(int(total) + 1000)
    else:
        print(total)
key(str(input()))


"""Key""" #ดิด
def main(num_id, total):
    """main"""
    for i in num_id:
        total += int(i)
    hundred = (int(num_id) % 1000) * 10
    if total + hundred > 9999:
        print("%04d" % ((total + hundred) % 10000))
    elif total + hundred < 1000:
        print(total + hundred + 1000)
    else:
        print(total + hundred)
main(input(), 0)