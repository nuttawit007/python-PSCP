"""Week10"""
def main(width):
    """Diamond I"""
    input()
    sum_num = []
    for row in range(width):
        num = input().split()
        # ให้แถวแรกเป้ฯตัวตั้งใส่ไปใน list ก่อน
        if row == 0:
            for item in num:
                sum_num.append(int(item))
        # แถวต่อๆมาทำการบวกเพิ่มเข้าไปแล้วเก็บไว้ที่ sum_num
        else:
            _round = 0
            for item in num:
                sum_num[_round] = sum_num[_round] + int(item)
                _round += 1
            _round = 0
    # เพชรที่มีค่ามากสุด
    print(max(sum_num))
main(int(input()))


"""Diamond I""" #ดิด
def main(row, column):
    """main"""
    my_list = []
    for k in range(row):
        num = [int(x) for x in input().split(" ")]
        if k == 0:
            my_list.extend(num)
        else:
            for i in range(column):
                my_list[i] = my_list[i] + num[i]
    print(max(my_list))
main(int(input()), int(input()))