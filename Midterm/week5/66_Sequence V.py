"""Week 5"""
def main(num):
    """Sequence V"""
    con = -1
    for i in range(num, 0, -1):
        con += 1
        if con == 0:
            print(i, end=' ')
        elif con % 7 == 0:
            print()
            print(i, end=' ')
        else:
            print(i, end=' ')
main(int(input()))



"""Sequence V""" #ตะวัน
def sequence():
    """Print from num to 1"""
    start = int(input())
    for num in range(start, 0, -1):
        #เงื่อนไขการขึ้นบรรทัดใหม่ >> 1.ไม่เท่ากับเลขเริ่ม 2.เลขนั้นๆกับเลขเริ่ม (% 7)ต้องเท่ากัน >> ครบ7ตัวขึ้นบรรทัดใหม่
        if num != start and num%7 == start%7:
            print()
        print(num, end=" ")
sequence()