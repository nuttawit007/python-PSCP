"""Week 5""" #***
import math
def align(size, alignment, txt):
    """Align"""
    if alignment == "left":
        print(txt)
    elif alignment == "right":
        print(txt.rjust(size))
    elif alignment == "center":
        gap = size - len(txt)
        left = math.ceil(gap/2)
        right = math.floor(gap/2)
        print(" "*left + txt + " "*right)
align(int(input()), input(), input())

"""
.rjust(ช่องว่าง) >> ชิดขวา
"""

"""Align""" #ดิด
def main():
    """main"""
    size = int(input())
    pos = input()
    txt = input()
    if pos == "center":
        print(" "* ((size - len(txt)) % 2) + txt.center(size - ((size - len(txt)) % 2)))
    elif pos == "left":
        print(txt.ljust(size))
    else:
        print(txt.rjust(size))
main()