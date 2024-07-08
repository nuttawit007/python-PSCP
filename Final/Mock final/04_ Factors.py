"""Factors 04"""
def prime_factors(n):
    """Find factor"""
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors

def pattern(number):
    """Factors pattern"""
    number = "".join(map(str, prime_factors(number)))
    dic_socks = {}
    factors = []
    for num in number:
        dic_socks[num] = dic_socks.get(num, 0) + 1
    for key, val in dic_socks.items():
        if val > 1:
            factors.append(str(key)+"**"+str(val))
        else:
            factors.append(str(key))
    return " x ".join(factors)

def main(number):
    """Factors"""
    for _ in range(number):
        num = int(input())
        print(pattern(num))
main(int(input()))
