"""Week 7"""
def main(top, potato, bottom, finger):
    """[Midterm 2020] Pringles"""
    catch = potato[:finger]
    left = potato[finger:]
    eat = 0
    for chip in catch:
        if chip == ")":
            eat += 1
    catch = catch.replace(")", " ")
    total_left = catch + left
    print(eat)
    if total_left.count(")") == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(top)
    print(total_left)
    print(bottom)
main(input(), input(), input(), int(input()))
