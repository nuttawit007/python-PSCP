"""Duplicate I"""
def main(quan_a, quan_b):
    """Duplicate I"""
    set_a = {int(input()) for _ in range(quan_a)}
    set_b = {int(input()) for _ in range(quan_b)}
    same = set_a.intersection(set_b)
    sort_descent_set = sorted(same, reverse=True)
    if len(same) == 0:
        print("Nsope")
    else:
        for num in sort_descent_set:
            print(num)
main(int(input()), int(input()))
