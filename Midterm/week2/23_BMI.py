"""BMI"""
def main(num):
    """BMI"""
    if num == 0:
        return
    else:
        name = input()
        weight = float(input())
        high = float(input())
        bmi = weight/((high/100)**2)
        print(name + "'s  BMI = %.2f" % bmi)
        main(num-1)
main(5)
