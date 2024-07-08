"""Week10"""
def display(amount):
    """Show -"""
    style = ""
    for num in range(1, amount+1):
        if num%5 == 1 and num != 1:
            style += "|-"
        else:
            style += "-"
    return style

def main(text):
    """HorizontalHistogram"""
    list_letter = set([letter for letter in text]) # เก็บเป็น set เพราะไม่เอาตัวซ้ำ เวลาไป sorted
    sort_letter = sorted(list_letter, key=str.swapcase)
    for letter in sort_letter:
        amount = text.count("%s" % letter)
        print(letter, ":", display(amount))
main(input())

"""
การ sorted ตัวอักษร พิมพ์ใหญ่ >> พิมพ์เล็ก: mysort = sorted(data)
การ sorted ตัวอักษร พิมพ์เล็ก >> พิมพ์ใหญ่: my_sort = sorted(data, key=str.swapcase)
"""