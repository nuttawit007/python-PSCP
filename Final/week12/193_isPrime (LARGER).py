"""Week 12"""
def main(num):
    """isPrime_(LAERGER)"""
    count = 0
    if num == 1:
        count += 1
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                count += 1
                break
    if count == 1:
        print(False)
    else:
        print(True)
main(int(input()))
