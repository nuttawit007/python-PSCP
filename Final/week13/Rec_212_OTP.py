"""Week 13"""
def main():
    """OTP"""
    while True:
        otp = input()
        if otp == "0":
            break
        dic_num = {}
        for num in otp:
            dic_num[num] = dic_num.get(num, 0) + 1
        value_num = list(dic_num.values())
        if len(otp) == 4 and value_num.count(2) == 1:
            print("Valid")
        elif len(otp) == 6 and (value_num.count(2) == 2 or value_num.count(3) == 1):
            print("Valid")
        elif len(otp) == 8 and (value_num.count(2) == 3 or value_num.count(3) == 2):
            print("Valid")
        else:
            print("Invalid")
main()
