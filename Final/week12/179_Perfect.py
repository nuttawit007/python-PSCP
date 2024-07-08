"""Week 12"""
def isperfect(num):
    """is number is perfect number"""
    use_num = num
    """ perfect คือ ตัวหารที่สามารถหารตัวเลขนั้นลงตัว (แต่ไม่รวมตัวมันเอง) เท่ากับมันเอง:
        6 เป็น Perfect number เพราะ proper divisors ของ 6 คือ 1, 2, 3 ซึ่งผลรวมมีค่าเท่ากับ 6
    """
    # loop แค่ root num + 1 เพื่อให้ไม่ time out
    """
        checkโดย : ลบเลขที่มันหารลงตัว กับ เลขที่มันหารลงตัวอีกตัวนึง เพื่อให้ลดจำนวนloopลง
        เช่น 6%2 ลงตัว จะลบ 2 และ 3 ในทีเดียว
        โดยจะเป็น perfect ถ้าลบแล้วเหลือ 1 เพราะ 1 เป็นตัวประกอบเสมอ
    """
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            use_num -= i + (num//i)
        if use_num < 1:
            break
    # เลข 1 ไม่นับเป็น perfect เพราะจะไม่รวมตัวเอง
    if use_num == 1 and num != 1:
        return num
    else:
        return 0

def main(num):
    """Perfect"""
    val_perfect = 0
    for i in range(1, num+1):
        val_perfect += isperfect(i)
    print(val_perfect)
main(int(input()))
