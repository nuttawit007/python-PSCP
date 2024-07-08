"""[Midterm 2023] Lift"""
def lift(people, highweight):
    """[Midterm 2023] Lift"""
    totalweight = 0
    more12, less12 = 0, 0
    for _ in range(people):
        age = int(input())
        if age >= 12:
            more12 += 1
        else:
            less12 += 1
        weight = float(input())
        totalweight += weight
    if totalweight > highweight:
        print("Not Safe")
    elif less12 > 0 and more12 == 0:
        print("Not Safe")
    else:
        print("Safe")
lift(int(input()), float(input()))
