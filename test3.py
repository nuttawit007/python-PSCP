def prime_factors(n):
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors

num = int(input("ป้อนตัวเลข: "))
factors = prime_factors(num)
print(f"ตัวประกอบจำนวนเฉพาะของ {num} คือ {factors}")
