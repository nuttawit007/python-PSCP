"""Week 15"""
def main():
    """Sort(Insertsort)"""
    all_num = []
    while True:
        num = input()
        if num == "END":
            break
        all_num.append(float(num))
    all_num = list(map(int, all_num))
    # insertion sort
    for i in range(len(all_num)):
        if i == 0:
            continue
        for j in range(i-1, -1, -1):
            if all_num[i] < all_num[j]:
                all_num.insert(j, all_num[i])
                del all_num[i]
    print(all_num)
main()