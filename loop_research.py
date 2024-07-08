"""ตัวเลข"""
# ขวาบน
num = int(input())
for row in range(1, num+1):
    for col in range(1, row+1):
        print(col, end="")
    print()

# ขวาล่าง
num = int(input())
for row in range(num):
    for col in range(1, (num+1)-row):
        print(col, end="")
    print()

# ซ้ายบน
num = int(input())
for row in range(1, num+1):
    # space
    for col in range(num-row):
        print(" ", end="")
    # number
    for col in range(1, row+1):
        print(col, end="")
    print()

#ซ้ายล่าง
num = int(input())
for row in range(num):
    for col in range(row):
        print(" ", end="")
    for col in range(1, (num+1)-row):
        print(col, end="")
    print()


""""ดาว"""
# ขวาบน
num =int(input())
for row in range(1, num+1):
    for col in range(row):
        print("*", end="")
    print()

# ขวาล่าง
num = int(input())
for row in range(num):
    for col in range(num-row):
        print("*", end="")
    print()

# ซ้ายบน
num = int(input())
for row in range(1, num+1):
    for col in range(num-row):
        print(" ", end="")
    for col in range(1, row+1):
        print("*", end="")
    print()

# ซ้ายล่าง
num = int(input())
for row in range(num):
    for col in range(row):
        print(" ", end="")
    for col in range(num-row):
        print("*", end="")
    print()

"""Sequence VII"""
num = int(input())
for row in range(1, num+1):
    for col in range(1, row+1):
        print(col, end="")
    print()
for row in range(1, num):
    for col in range(1, (num+1)-row):
        print(col, end="")
    print()

"""Sequence VIII"""
num = int(input())
for row in range(1, num+1):
    for col in range(num-row):
        print("   ", end="")
    for col in range(1, row+1):
        print("%02d " % col, end="")
    print()

"""Sequence IX"""
num = int(input())
for row in range(1, num+1):
    for col in range(num-row):
        print("   ", end="")
    for col in range(1, row+1):
        print("%02d " % col, end="")
    for col in range(row-1):
        print("%02d " % (col+1),end="")
    print()

"""Sequence X"""
num = int(input())
# upper pyramid
for row in range(1, num+1):
    # top left
    for col in range(num-row):
        print("   ", end="")
    for col in range(1, row+1):
        print("%02d " % col, end="")
    # top right
    for col in range(row-1, 0, -1):
        print("%02d " % col, end="")
    print()
# lower pyramid
for row in range(num-1):
    # btm left
    for col in range(row+1):
        print("   ", end="")
    for col in range(1, num-row):
        print("%02d " % col, end="")
    # btm right
    for col in range((num-2)-row, 0, -1):
        print("%02d " % col, end="")
    print()