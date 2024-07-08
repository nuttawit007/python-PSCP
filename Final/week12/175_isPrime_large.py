"""Week 12"""
import math
def main(num):
    """isprime_large"""
    """prime number : สามารถเช็คได้ว่าเป็นไม่เป็นโดย loop แค่ root num"""
    count = 0
    if num == 1:
        count += 1
    else:
        # loop แค่ root num + 1 เพราะ จะได้ไม่ time out 
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                count += 1
                break
    if count == 1:
        print("NO")
    else:
        print("YES")
main(int(input()))
