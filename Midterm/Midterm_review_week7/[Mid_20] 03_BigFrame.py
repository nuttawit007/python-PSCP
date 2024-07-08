"""Week 7"""
def bigframe(txt1, txt2, txt3, txt4, txt5):
    """[Midterm 2020] BigFrame"""
    long_text = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
    for row in range(7):
        if row == 0 or row == 6:
            print("*" * (long_text+4))
        elif row == 1:
            print("* " + txt1 + " "*(long_text-len(txt1)) + " *")
        elif row == 2:
            print("* " + txt2 + " "*(long_text-len(txt2)) + " *")
        elif row == 3:
            print("* " + txt3 + " "*(long_text-len(txt3)) + " *")
        elif row == 4:
            print("* " + txt4 + " "*(long_text-len(txt4)) + " *")
        elif row == 5:
            print("* " + txt5 + " "*(long_text-len(txt5)) + " *")
bigframe(input().strip(), input().strip(), input().strip(), input().strip(), input().strip())
