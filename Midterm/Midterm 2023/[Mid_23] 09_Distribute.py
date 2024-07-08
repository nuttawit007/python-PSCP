"""[Midterm 2023] Distribute"""
def main(money, people):
    """[Midterm 2023] Distribute"""
    if money < people:
        return -1
    if people == 1 and money > 8:
        return 0
    money -= people
    eight = money//7
    if money%7 == 3 and people - eight == 1:
        eight -= 1
        return eight
    elif eight > people:
        return people-1
    elif money%7 > 0:
        if eight - people == 0:
            return eight-1
        else:
            return eight
    else:
        return eight
print(main(int(input()), int(input())))
