# """Week 4"""
# def main(number):
#     """BootSequence"""
#     result = "_".join(str(_) for _ in range(1, number+1))
#     print(result)
# main(int(input()))
"""BootSequence"""
def sequence():
    """Print number with _"""
    stop = int(input())
    print(*range(1, stop+1), sep="_")

sequence()