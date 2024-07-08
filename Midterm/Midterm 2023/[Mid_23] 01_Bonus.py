"""[Midterm 2023] Bonus"""
def main(salary, year, month):
    """[Midterm 2023] Bonus"""
    bonus = year
    if month//10 != 0:
        bonus += 1
    if bonus > 20:
        bonus = 20
    total_bonus = salary*bonus
    if total_bonus > 1000000:
        total_bonus = 1000000
    elif total_bonus < 5000:
        total_bonus = 5000
    print(total_bonus)
main(int(input()), int(input()), int(input()))
