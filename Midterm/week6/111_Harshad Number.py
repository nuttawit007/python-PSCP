"""Week 6""" #***
def harshad_num():
    """Harshad Number"""
    for _ in range(10):
        num = input()
        digit_sum = 0
        if int(num) < 0: #กรณีเลขติดลบ
            num = num.replace("-", "")
        for number in num:
            digit_sum += int(number)
        if int(num) == 0:
            print("No")
        elif int(num) % digit_sum == 0:
            print("Yes")
        else:
            print("No")
harshad_num()
