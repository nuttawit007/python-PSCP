"""final 08"""
def main(socks):
    """Socks"""
    dic_socks = {}
    for i in socks:
        dic_socks[i] = dic_socks.get(i, 0) + 1
    lis_socks = []
    for key, val in dic_socks.items():
        couple = 0
        if val == 0:
            continue
        if val%2 == 0:
            couple += val//2
        else:
            couple += (val-1)//2
        for _ in range(couple):
            lis_socks.append(key*2)
    if len(lis_socks) > 0:
        for cou in sorted(lis_socks):
            print(cou, end=" ")
        print()
        print(len(lis_socks))
    else:
        print("None")
        print(0)
main(input())
