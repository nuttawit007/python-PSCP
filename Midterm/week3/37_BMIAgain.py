"""Week 3"""
def main(weight, high):
    """BMIAgain"""
    bmi = weight/((high/100)**2)
    if bmi >= 30:
        print("Obese")
    elif bmi >= 25:
        print("Overweight")
    elif bmi >= 18.5:
        print("Normal")
    elif bmi < 18.5:
        print("Underweight")
main(int(input()), int(input()))
