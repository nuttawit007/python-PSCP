# """Week 5""" #***
# def main(num):
#     """Sequence VII"""
#     val = []
#     for i in range(1, num+1):
#         val.append(str(i))
#         print(" ".join(val))
#     for _ in range(1, num):
#         val.pop(-1)
#         print(" ".join(val))
# main(int(input()))


"""Sequence VII"""
def pyramid():
    """Make pyramid"""
    width = int(input())
    #Top Half
    for row in range(width):
        for col in range(row+1):
            print(col+1, end=" ")
        print()
    #Bottom Half
    for row in range(1, width):
        for col in range(width-row):
            print(col+1, end=" ")
        print()
pyramid()