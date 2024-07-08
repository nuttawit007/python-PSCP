"""Week 6""" #***
def decode(coding):
    """Run Length Decoding"""
    decoding = ""
    for text in coding:
        if text.isdecimal():
            decoding += text
        else:
            print(text * int(decoding), end="")
            decoding = ""
decode(input())
