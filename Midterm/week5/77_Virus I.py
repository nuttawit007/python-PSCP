"""Week 5"""
def main(txt):
    """Virus I"""
    box = 0
    for letter in txt:
        if letter == "o":
            box += 1
    print(box)
main(str(input()))
