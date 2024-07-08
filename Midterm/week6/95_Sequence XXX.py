"""Week 6""" #*****
# def main():
#     """Sequence XXXX"""
#     size = int(input())
#     num = int(input())
#     for i in range(size):
#         if i == 0 or i == size-1:
#             for _ in range(num):
#                 print("*"*size, end=" ")
#             print()
#         else:
#             for _ in range(num):
#                 for j in range(size):
#                     if i == j or j == 0 or j == size-1 or j == size-1-i:
#                         print("*", end="")
#                     else:
#                         print(" ", end="")
#                 print("", end=" ")
#             print()
# main()

"""This one is hard"""
def draw(dimen, amount):
    """My idea is to draw one row and multiply"""
    for row in range(dimen):
        out = ""
        for col in range(dimen):
            if row == 0 or col == 0 or row == dimen-1 or col == dimen-1 or row == col or col == (dimen-1)-row:
                out += "*"
            else:
                out += " "
        out += " "
        print(out*amount)
draw(int(input()), int(input()))