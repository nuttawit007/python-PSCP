"""week 10""" #***
def main():
    """week10"""
    text = input()
    set_text = set(text)
    sort_text = sorted(set_text, key=str.lower)
    for cha in sort_text:
        if cha.islower():
            print(cha, "=", text.count("%s" % cha))
            if cha.upper() in sort_text:
                print(cha.upper(), "=", text.count("%s" % cha.upper()))
                sort_text.remove(cha.upper())
        elif cha.isupper():
            if cha.lower() in sort_text:
                print(cha.lower(), "=", text.count("%s" % cha.lower()))
                print(cha, "=", text.count("%s" % cha))
                sort_text.remove(cha.lower())
            else:
                print(cha, "=", text.count("%s" % cha))
main()
