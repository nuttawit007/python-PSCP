"""Week 11"""
def find_gcd(num1, num2):
    """Find GCD"""
    if num2 == 0:
        return num1
    else:
        return find_gcd(num2, num1%num2)

def main(num1, num2):
    """CoPrimeV1"""
    if find_gcd(num1, num2) == 1:
        print("YES")
        print(find_gcd(num1, num2))
    else:
        print("NO")
        print(find_gcd(num1, num2))
main(int(input()), int(input()))
