"""Week 7"""
def bts(day, age, high):
    """[Midterm 2020] BTSMRT"""
    if age < 14 and high < 90:
        print("FREE")
    elif day == "Children Day" and age < 14 and high <= 140:
        print("FREE")
    elif day == "Senior Day" and age >= 60:
        print("FREE")
    else:
        print("PAY")
bts(input(), float(input()), float(input()))
