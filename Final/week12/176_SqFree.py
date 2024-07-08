"""Week 12"""
def sqfree(var_a):
    """isSqFree"""
    """sqfree : ไม่มี b >= 2 and a%b**2 == 0"""
    """
        checkโดย : loop แค่เพียง root num ก็เพียงพอเปรียบเสมือน prime number
    """
    count = 0
    if var_a == 1: # 1 เป็น sqfree แน่นอน
        pass
    else:
        # loop แค่ root num + 1 เพราะ จะได้ไม่ time out 
        for var_b in range(2, int(var_a**0.5)+1):
            # ถ้ามี b**2 ไหนหารลง จะไม่ใช่ sqfree ทันที
            if var_a%(var_b**2) == 0:
                count += 1
                break
    return 0 if count == 1 else 1

def main(quan):
    """SqFree"""
    count = 0
    for num in range(1, quan+1):
        count += sqfree(num)
    print(count)
main(int(input()))
