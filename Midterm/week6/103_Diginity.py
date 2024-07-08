"""Week 6"""
def main():
    """Diginity"""
    while True:
        num = input()
        if num == "0":
            break
        _round, new_num = 0, num
        while _round < len(num):
            digit_sum = 0
            for number in new_num:
                digit_sum += int(number)
                new_num = str(digit_sum)
            _round += 1
        print(digit_sum)
main()
