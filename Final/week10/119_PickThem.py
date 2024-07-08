"""PickThem"""
def main():
    """PickThem"""
    stock = input().replace("[", "").replace("]", "")
    stock = stock.split(", ")
    # stock = input().strip("[]").split(", ")
    even_num = []
    for num in stock:
        if int(num)%2 == 0:
            even_num.append(num)
    if len(even_num) == 0:
        print("Nope")
    else:
        for num in even_num:
            print(num)
main()

"""
เอาตัวอักษรที่ไม่ต้องการออกจาก str ที่รับเบข้ามา >> .strip()
    stock = input().strip("[]").split(", ")
"""