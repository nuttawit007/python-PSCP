"""Week 6""" #*****
# def main():
#     """FourDirections"""
#     password = input()
#     for row in range(len(password)):
#         line1()
#     print()
#     for row in range(len(password)):
#         line2(password, row)
#     print()
#     for row in range(len(password)):
#         line3(password, row)
#     print()
#     for row in range(len(password)):
#         line4(password, row)
#     print()
#     for row in range(len(password)):
#         line1()
#     print()

# def line1():
#     """Line1"""
#     print("  *  ", end=" ")

# def line2(password, roundnum):
#     """Line2"""
#     if password[roundnum] == "U":
#         print(" *** ", end=" ")
#     elif password[roundnum] == "D":
#         print("  *  ", end=" ")
#     elif password[roundnum] == "L":
#         print(" *   ", end=" ")
#     elif password[roundnum] == "R":
#         print("   * ", end=" ")

# def line3(password, roundnum):
#     """Line3"""
#     if password[roundnum] in "UD":
#         print("* * *", end=" ")
#     elif password[roundnum] in "LR":
#         print("*****", end=" ")

# def line4(password, roundnum):
#     """Line4"""
#     if password[roundnum] == "U":
#         print("  *  ", end=" ")
#     elif password[roundnum] == "D":
#         print(" *** ", end=" ")
#     elif password[roundnum] == "L":
#         print(" *   ", end=" ")
#     elif password[roundnum] == "R":
#         print("   * ", end=" ")
# main()

"""fourdirection"""
def fourdirec(direction):
    """4ทิศพิชิตเธอ"""
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""
    line_5 = ""
    for i in direction:
        if i == "U":
            line_1 += "  *   "
            line_2 += " ***  "
            line_3 += "* * * "
            line_4 += "  *   "
            line_5 += "  *   "
        elif i == "D":
            line_1 += "  *   "
            line_2 += "  *   "
            line_3 += "* * * "
            line_4 += " ***  "
            line_5 += "  *   "
        elif i == "L":
            line_1 += "  *   "
            line_2 += " *    "
            line_3 += "***** "
            line_4 += " *    "
            line_5 += "  *   "
        elif i == "R":
            line_1 += "  *   "
            line_2 += "   *  "
            line_3 += "***** "
            line_4 += "   *  "
            line_5 += "  *   "
    print(line_1, line_2, line_3, line_4, line_5, sep="\n")
fourdirec(direction=input())