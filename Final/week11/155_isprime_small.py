"""Week11"""
def main(num):
    """isprime_small"""
    count = 0
    for i in range(2, num+1):
        if num%i == 0:
            count += 1
    if count == 1:
        print("Yes")
    else:
        print("No")
main(int(input()))
