"""Week 13"""
def main(age, weight, donate):
    """BloodDonation"""
    if age == 17 or 60 <= age <= 70:
        confirm = input()
    if age < 17 or age > 70 or weight < 45:
        print("No")
    elif donate == 0 and age > 55:
        print("No")
    elif age == 17 and confirm == "False":
        print("No")
    elif 60 <= age <= 70 and confirm == 'False':
        print("No")
    else:
        print("Yes")
main(int(input()), int(input()), int(input()))
