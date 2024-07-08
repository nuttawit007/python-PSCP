# x = [1, 3, 4, 6, 3, 4]
# sort_x = [ _ for _ in sorted(x)]
# diff = [abs(sort_x[i] - sort_x[i+1]) for i in range(0, len(sort_x), 2)]
# y = 0
# for i in diff:
#     y = y + i
# # print(y)

# def funf(aaa):
#     """TheFunctionWithin"""
#     return aaa/45
# def main(aaa):
#     """TheFunctionWithin"""
#     print(funf(aaa))
# main(float(input()))

# import math
# print(math.ceil(1/2))



# def main(score, high_score):
#     """Surprise"""
#     left_score = score - high_score
#     if left_score/2 < high_score-1:
#         print("Surprising")
#     else:
#         print("Not surprising")
# main(float(input()), float(input()))

# mylotto = input()
# last2_lot = input()
# total_prize = 0
# if (int(mylotto)%1000) == int(last2_lot):
#         total_prize += 2000
# print(total_prize)

# phone = "096741477"
# pattern = phone[0] +" "+ phone[1:5] +" "+ phone[5:]
# inter = "+66"
# print(inter + pattern[1:])
# print(len("Hello world"))

# long_text = 7
# txt1 = "win"
# print("* " + txt1 + " "*(long_text-len(txt1)) + " *")
# long_text = len(max("win", "jame"))
# print(long_text)

# name = [input() for _ in range(5)]
# print(name)
# potato = ")))) )))|"
# finger = 3
# catch = potato[:finger]
# left = potato[finger:]
# catch = catch.replace(")", " ")
# print(catch)
# print(left)
# print(catch + left)\
# ping = "ping www.facebook.com"
# print(ping[ping.find(" ")+1:ping.find(" ")+2])


# text = "refer"
# if text == text[::-1]:
#     print(text, "is palindrome")

"""[::-1] >> เอาตั้งแต่ตัวแรกถึงตัวสุดท้ายแต่ย้อนกลับ"""
# num = int(input())
# for i in range(-num + 1, num, 1):
#     print(i)
# def main(money):
#     b1000 = money//1000
#     money = money%1000
#     b500 = money//500
#     money = money%500
#     b100 = money//100
#     print(b1000, b500, b100)
# main(int(input()))
# num = float(input())
# num = int(num*100)/100
# print("%.2f" % num)


# print(*range(1,6), sep="_")
# print(round(2.5))
# print(round(3.5))
# print(round(4.5))
# print(type(eval("2.45")))
# name = "win\teat\tdinner"
# print(len(name.expandtabs(1)))
# print(len(name.expandtabs(2)))

# num = [1,2,3,4,5]
# print(max(num))
# quantity = int(input())
# data = [input().split("\t") for _ in range(quantity)]
# only_score = [score[1] for score in data]
# total_score = 0
# for score in only_score:
#     total_score += float(score)
# print(total_score)

# text = tuple(input().split())
# txt_index = text.index("2")
# txt_count = text.count("2")
# print(text)
# print(txt_index)
# print(txt_count)
# num1 = [1, 2]
# num2 = [3, 4]
# for i in range(2):
#     num1[i] = num1[i] + num2[i]
# print(num1)

# cat = ["a", "g", "v"]
# cat1 = ["a", "g", "v"]
# cat = cat.remove()
# print(cat)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# """loop value """
# for val in car.values():
#     print(val)

# """loop key"""
# for key in car:
#     print(key)
#     print(type(key))
# dick = {}
# data = input().strip("{}").split(" : ")
# dick[data[0]] = data[1]
# print(dick)


# สร้าง dictionary เปล่า
# my_dict = {}

# # รับข้อมูลจากผู้ใช้
# k_v = ["name", "win", "age", "19"]


# # เพิ่มข้อมูลใน dictionary
# for i in range(0, 3, 2):
#     my_dict.update({k_v[i]: k_v[i+1]})
#     # print(i)

# # # แสดง dictionary ที่สร้าง
# # print(my_dict)
# print(343//7)
# # dict_num = {1 : "Sunday"}
# # print(dict_num[1])
# dict_month = {1 : 0, 2 : 31, 3 : 59, 4 : 90, 5 : 120, 6 : 151, 7 : 181, 8 : 212, 9 : 243, 10 : 273, 11 : 304, 12 : 334}
# print(dict_month[12])

# text = input()
# split_num = ""
# for cha in text:
#     if cha.isdigit() == False:
#         split_num += " "+cha+" "
#     else:
#         split_num += cha
# list_num = [int(num) for num in split_num.split() if num.isdigit()]
# total_sum = sum(list_num)
# print(split_num)
# print(list_num)
# print(total_sum)

"""ลืม"""
# char = input()
# if char.isupper():
#     start = 65 - (ord(char)-3)
#     if start > 0:
#         print(chr(91-start))
#     else:
#         print(chr(ord(char)-3))
# elif char.islower():
#     start = 97 - (ord(char)-3)
#     if start > 0:
#         print(chr(122-start))
#     else:
#         print(chr(ord(char)-3))

"""Week 12"""
def main():
    """Gram_v1"""
    # นับว่าแต่ละแบบมีกี่ตัว
    text = input()
    style1 = text.count('WO')
    style2 = text.count('WW')
    style3 = text.count('OW')
    # เก็บไว้ใน dict
    all_style = {}
    if style1 > 0:
        all_style["WO"] = style1
    if style2 > 0:
        all_style["WW"] = style2
    if style3 > 0:
        all_style["OW"] = style3
    # จำนวนที่มีมากสุด
    max_val = max(all_style.values())
    # หา index ของตัวมากสุด
    index_maxval, use_text = {}, text
    for key, val in all_style.items():
        if val == max_val:
            use_text = list(use_text.replace(key, "$"))
            index_maxval[key] = use_text.index("$")
            use_text = text
    # ตัวแรกที่เจอ
    first_index = min(index_maxval.values())
    for key, val in index_maxval.items():
        if val == first_index:
            print(key)
            print(all_style[key])
main()


def main(distance, quan):
    """Runner"""
    all_people = [tuple(map(int, input().split())) for _ in range(quan)]
    winner = sorted(all_people, key=lambda x: ((distance-x[1])/x[0])-x[0])
    print(all_people.index(winner[0])+1)
main(int(input()), int(input()))
