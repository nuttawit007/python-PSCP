""""Difference"""
def main(quan_a, quan_b):
    """Difference"""
    set_a = {int(input()) for _ in range(quan_a)}
    set_b = {int(input()) for _ in range(quan_b)}
    diff = set_a - set_b
    sort_ascent_set = sorted(diff)
    for num in sort_ascent_set:
        print(num, end=" ")
main(int(input()), int(input()))

"""
    sorted >> ต้องมีตัวแปรมารับ ไม่เปลี่ยนต้นฉบับ
    sort >> ไม่ต้องมีตัวแปรมารับ เปลี่ยนต้นฉบบับ
"""