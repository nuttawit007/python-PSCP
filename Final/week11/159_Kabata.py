"""week 11"""
def main(quan):
    """Kabata"""
    for _ in range(quan):
        text = input().replace("baka", "no").replace("bakka", "").replace("ba", "")\
        .replace("ka", "").replace("ta", "")
        if text == "":
            print("yes")
        else:
            print("no")
main(int(input()))
