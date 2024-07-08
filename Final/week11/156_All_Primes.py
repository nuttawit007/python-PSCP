"""Week11"""
def isprime(num):
    """check is prime"""
    count = 0
    for i in range(2, num+1):
        if num%i == 0:
            count += 1
    if count == 1:
        return "Yes"
    else:
        return "No"

def main(num):
    """All_Primes"""
    prime = 0
    for i in range(2, num+1):
        if isprime(i) == "Yes":
            prime += 1
    print(prime)
main(int(input()))
