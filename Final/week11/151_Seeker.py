"""Week11"""
def sep_num(text):
    """sep text or num"""
    split_num = ""
    for cha in text:
        if cha.isdigit() == False:
            split_num += " "+cha+" "
        else:
            split_num += cha
    return split_num

def main():
    """Seeker"""
    text = input()
    list_num = [int(num) for num in sep_num(text).split() if num.isdigit()]
    total_sum = sum(list_num)
    print(total_sum)
main()
