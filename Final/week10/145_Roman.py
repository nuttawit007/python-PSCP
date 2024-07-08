"""Week10"""
def main():
    """Roman"""
    roman_num = input()
    roman_val = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    # เอาแต่ละค่าเก็บไว้ใน list
    num_val = []
    for num in roman_num:
        num_val.append(roman_val[num])
    total_roman = 0
    # setdefult เป็น ค่าตัวสุดท้ายของเลข roman
    old_num = num_val[-1]
    # loop ไล่จากหนักสุดท้าย ถ้ามีค่าน้อยกว่าตัวก่อนหน้าให้ลบออก
    for num in num_val[::-1]: 
        if num < old_num:
            total_roman -= num
        else:
            total_roman += num
        old_num = num
    print(total_roman)
main()
