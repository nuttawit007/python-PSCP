"""Week 12"""
def find_gcd(number1, number2):
    """find GCD"""
    if number2 == 0:
        return number1
    else:
        return find_gcd(number2, number1 % number2)

def main(num1, num2):
    """GCD"""
    result = find_gcd(num1, num2)
    print(result)
main(int(input()), int(input()))
