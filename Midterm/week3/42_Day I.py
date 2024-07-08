"""Week 3"""
def main(year):
    """Day I"""
    if year % 100 == 0 and year % 400 != 0:
        print("No")
    elif year % 4 == 0:
        print("Yes")
    else:
        print("No")
main(int(input()))
