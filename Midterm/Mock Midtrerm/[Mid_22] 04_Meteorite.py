"""Week 7"""
def main(weight, sub_unit, save):
    """[Midterm 2022] Meteorite"""
    unit_weight, rocket, _round, new_weight = 0, 0, 0, weight
    while True:
        if weight < save:
            break
        unit_weight = new_weight/sub_unit
        new_weight = unit_weight
        rocket += (sub_unit**_round)
        _round += 1
        if new_weight < save:
            break
    print(rocket)
main(float(input()), int(input()), float(input()))
