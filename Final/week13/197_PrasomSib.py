"""Week 13"""
def main(number):
    """PrasomSib"""
    ten, count = 0, 0
    for i in range(len(number)):
        ten = int(number[i])
        for j in range(i+1, len(number)):
            ten += int(number[j])
            if ten == 10:
                count += 1
                break
            elif ten > 10:
                break
    print(count)
main(input())
