"""Week 10"""
def main():
    """VerticalHistogram"""
    text = input()
    alpa = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = {}
    for alpha in alpa:
        result[alpha] = 0
        for char in text:
            if char == alpha:
                result[alpha] += 1
    maximum = result[max(result, key=result.get)]
    for count in range(maximum, 0, -1):
        print("%03d" %count, end='')
        for alpha in alpa:
            if result[alpha] >= count and result[alpha] != 0:
                print(" *", end='')
            elif result[alpha] == 0:
                continue
            else:
                print("  ", end='')
        print()
    print(" " * 3, end='')
    for alpha in alpa:
        if result[alpha] != 0:
            print(" %s" %alpha, end='')
main()


'''VerticalHistogram''' #poom
def _sort(ite):
    '''sort a-z -> A-Z'''
    return ord(ite[0]) + ord(ite[0])*(ite[0].isupper())
def vertical_histogram(text):
    '''VerticalHistogram'''
    count = {}
    for i in text:
        count[i] = count.get(i, 0) + 1
    count = dict(sorted(list(count.items()), key=_sort))
    for j in range(max(iter(count.values())), 0, -1):
        print("%03d"%(j), *["*"*(i >= j) or " " for i in iter(count.values())])
    print("   ", *list(count.keys()))
vertical_histogram(iter(input()))
