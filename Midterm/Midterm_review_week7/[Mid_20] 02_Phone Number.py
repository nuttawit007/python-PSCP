"""Week 7"""
def phone_num(phone, local):
    """[Midterm 2020] Phone Number"""
    if len(phone) == 10:
        pattern = phone[:2] +" "+ phone[2:6] +" "+ phone[6:]
    else:
        pattern = phone[0] +" "+ phone[1:5] +" "+ phone[5:]
    if local == "Domestic":
        print(pattern)
    elif local == "International":
        inter = "+66"
        print(inter + pattern[1:])
phone_num(input(), input())

# def main(phone, kind): #ออม
#     if kind == "International":
#         print("+66"+phone[1:-8], phone[-8:-4], phone[-4:])
#     else:
#         print(phone[:-8], phone[-8:-4], phone[-4:])
# main(input(), input())
