"""Week 4"""
def main(num):
    """HowLong"""
    _sum = 0
    #ใส่ abs() >> กรณีเลขติดลบ
    for _ in str(abs(num)): 
        _sum += 1
    print(_sum)
main(int(input()))
