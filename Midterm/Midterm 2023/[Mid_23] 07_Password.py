""""[Midterm 2023] Password"""
import math
def check_pool(text):
    """check pool"""
    pool = 0
    small, big, digit, special = False, False, False, False
    for i in text:
        if i.islower():
            small = True
        elif i.isupper():
            big = True
        elif i.isdigit():
            digit = True
        elif i.isprintable() and not i.isdigit() and not i.isalpha():
            special = True
    if small:
        pool += 26
    if big:
        pool += 26
    if digit:
        pool += 10
    if special:
        pool += 32
    return pool
def cal_entropy(pool, lenght):
    """cal"""
    return math.log2(pool ** lenght)
def main(text):
    """main"""
    lenght = len(text)
    entropy = int(cal_entropy(check_pool(text), lenght))
    print(entropy)
    if entropy >= 128:
        print("Very Strong")
    elif 60 <= entropy <= 127:
        print("Strong")
    elif 36 <= entropy <= 59:
        print("Reasonable")
    elif 28 <= entropy <= 35:
        print("Weak")
    elif entropy < 28:
        print("Very Weak")
main(input())
