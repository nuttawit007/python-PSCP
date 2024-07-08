"""week 7"""
def main(address):
    """[Midterm 2021] MAC"""
    letter = "0123456789ABCDEFabcdef-:."
    for text in address:
        if text not in letter:
            print("ERROR")
            break
    if address.count("-") == 5 and len(address) == 17:
        print("VALID 1")
    elif address.count(":") == 5 and len(address) == 17:
        print("VALID 2")
    elif address.count(".") == 2 and len(address) == 14:
        print("VALID 3")
    else:
        print("ERROR")
main(input())
