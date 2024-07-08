"""Week 7"""
def squidgame():
    """[Midterm 2021] Squid Game"""
    score_a, score_b = 0, 0
    for _round in range(20):
        if _round <= 9:
            score_a += int(input())
        else:
            score_b += int(input())
    if score_a > score_b:
        print("B")
    elif score_b > score_a:
        print("A")
    else:
        print("AB")
squidgame()
