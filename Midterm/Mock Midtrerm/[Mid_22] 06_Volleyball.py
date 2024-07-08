"""Week 7"""
def main(set_score):
    """[Midterm 2022] Volleyball"""
    _set = 1
    set_a, set_b = 0, 0
    score_a, score_b = 0, 0
    for point in set_score:
        if score_a == 25 and score_b < 25:
            print("Set %d: A (%d) | B (%d)" % (_set, score_a, score_b))
            _set += 1
            set_a += 1
        elif score_b == 25 and score_a < 25:
            print("Set %d: A (%d) | B (%d)" % (_set, score_a, score_b))
            _set += 1
            set_b += 1
        elif score_a == score_b and score_a >= 24:
            pass
main(int(input()))
