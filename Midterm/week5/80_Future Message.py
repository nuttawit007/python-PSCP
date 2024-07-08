"""Week 5"""
def main(txt):
    """Future Message"""
    if txt.isdecimal():
        print("Number")
    elif txt.isupper():
        print("Uppercase")
    elif txt.islower():
        print("Lowercase")
    elif txt.istitle():
        print("Title")
    elif txt.isspace():
        print("Space")
    else:
        print("Other")
main(str(input()))
