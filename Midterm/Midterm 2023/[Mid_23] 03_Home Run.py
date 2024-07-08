"""[Midterm 2023] Home Run"""
def main(court, player):
    """[Midterm 2023] Home Run"""
    homerun = 0
    for _ in range(court):
        feild = float(input())
        if player > feild:
            homerun += 1
    print(homerun)
main(int(input()), float(input()))
