"""Week 12"""
def find_gcd(number1, number2):
    """find GCD"""
    if number2 == 0:
        return number1
    else:
        return find_gcd(number2, number1 % number2)

def main(quan):
    """GCD_N"""
    all_num = [int(input()) for _ in range(quan)]
    gcd = all_num[0] # setdefult ให้ gcd = ค่าแรกสุดไปก่อน
    for num in range(1, len(all_num)):
        gcd = find_gcd(gcd, all_num[num]) # เอาค่าgcd 2 ตัวแรกไปใช้ต่อเรื่อยๆจนเลขหมด
    print(gcd)
main(int(input()))
