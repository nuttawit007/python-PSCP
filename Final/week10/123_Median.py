"""Median"""
def main(_round):
    """Median"""
    lis_num = []
    for _ in range(_round):
        num = int(input())
        lis_num.append(num)
    lis_num.sort()
    if len(lis_num)%2 != 0:
        print("%.1f" % lis_num[_round//2])
    else:
        print("%.1f" % ((lis_num[_round//2-1]+lis_num[_round//2])/2))
main(int(input()))
