"""Week10"""
def main():
    """Cat Parade"""
    all_cat = []
    while True:
        cat = input()
        if cat == "END":
            break
        """
            .pop() >> ตัดตัวล่าสุดใน list ออก
            continue >> ทำการข้าม loop ไปครั้งต่อไปเลย ดังนั้น "IT'S A DOG" จะไม่เข้าไปใน all_cat
        """
        if cat == "IT'S A DOG":
            all_cat.pop()
            continue
        """
            กรณี input() มี 2 แบบ:
            1. Siamese
            2. American, Shorthair
            จะต้องมีการแยกการ append เข้าไปใน list โดยใช้ ", " ในการเช็ค
        """
        if "," in cat:
            cat = cat.split(", ")
            for _ in cat:
                all_cat.append(_)
        else:
            all_cat.append(cat)
    """ sortตัสอักษร >> ใช้ sorted() ปกติได้เลย """
    sort_cat = sorted(set(all_cat))
    for cat in sort_cat:
        print(cat, all_cat.index(cat)+1, all_cat.count(cat))
main()



"""อันเก่า"""
# def main():
#     """Cat Parade"""
#     lis_cat, same_cat = [], []
#     while True:
#         cat = input()
#         if cat == "END":
#             break
#         elif cat == "IT'S A DOG":
#             lis_cat = lis_cat[:-1]
#             continue
#         if "," in cat:
#             cat = cat.split(", ")
#             for its in cat:
#                 if its in lis_cat:
#                     same_cat.append(its)
#                     lis_cat.append(" ")
#                 elif its not in lis_cat:
#                     lis_cat.append(its)
#         else:
#             if cat in lis_cat:
#                 same_cat.append(cat)
#                 lis_cat.append(" ")
#             elif cat not in lis_cat:
#                 lis_cat.append(cat)
#     sort_dictionary = sorted(lis_cat)
#     for_count_cat = lis_cat + same_cat
#     for cat in sort_dictionary:
#         if cat != " ":
#             print(cat, lis_cat.index(cat)+1, for_count_cat.count("%s"%cat))
# main()
