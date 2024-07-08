"""Week 6"""
def ball(txt):
    """FORF-Ball"""
    cup_a, cup_b, cup_c = "Ball", " ", " "
    for letter in txt:
        if letter == "A":
            cup_a, cup_b = cup_b, cup_a
        elif letter == "B":
            cup_b, cup_c = cup_c, cup_b
        elif letter == "C":
            cup_a, cup_c = cup_c, cup_a
    if cup_a == "Ball":
        print(1)
    elif cup_b == "Ball":
        print(2)
    elif cup_c == "Ball":
        print(3)
ball(input())
