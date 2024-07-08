"""PickThemAgain"""
def main():
    """PickThemAgain"""
    lis_num = input().split()
    three_five = [num for num in lis_num if int(num)%3 == 0 or int(num)%5 == 0]
    three_five = three_five[::-1]
    if len(three_five) == 0:
        print("Nope")
    else:
        for num in three_five:
            print(num)
main()
