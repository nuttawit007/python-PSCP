"""Week 7"""
def main(time):
    """[Midterm] Century"""
    for _ in range(time):
        year = input()
        year_num = int(year[5:])
        if year[:4] == "B.E.":
            year_num -= 543
        if year_num < 0:
            print("ERROR")
        else:
            print(-(-year_num//100))
main(int(input()))
