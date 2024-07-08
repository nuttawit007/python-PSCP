"""Week 7"""
# def diamond(number):
#     """[Midterm 2020] Diamond"""
#     halfsize = number//2
#     for i in range(number):
#         for j in range(number):
#             if i == halfsize or i+j == halfsize or \
#                 j-i == halfsize or j == number-i+halfsize-1 or i-j == halfsize:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
# diamond(int(input()))

"""Diamond"""
def diamond(size): # 7
    """Print Diamond"""
    half = size // 2 # 3
    for row in range(-half, half + 1): # -3 -2 -1 0 1 2 3
        for col in range(-half, half + 1): # -3 -2 -1 0 1 2 3
            diff = abs(row) + abs(col)
            """
            row = -3 : 6 5 4 3 4 5 6
            row = -2 : 5 4 3 2 3 4 5
            row = -1 : 4 3 2 1 2 3 4
            row = 0  : 3 2 1 0 1 2 3
            row = 1  : 4 3 2 1 2 3 4
            row = 2  : 5 4 3 2 3 4 5
            row = 3  : 6 5 4 3 4 5 6
            """
            if row == 0 or half == diff:
                print('*', end='')
            else:
                print(' ', end='')
        print()
diamond(int(input()))
