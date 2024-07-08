"""Week 7"""
import math
def main(day, salary):
    """[Midterm 2021] Cha Cha Cha"""
    for _ in range(day):
        hours = math.ceil(float(input()))
        salary += hours*8720
    print(salary)
main(int(input()), 0)
