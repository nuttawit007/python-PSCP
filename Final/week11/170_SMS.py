"""Week 12"""
def text(button, num):
    """What text use dict"""
    if num == 7 or num == 9:
        num = (num-1)%4
    else:
        num = (num-1)%3
    text = {1 : ("del"), 2 : ("A", "B", "C"), 3 : ("D", "E", "F"),\
         4 : ("G", "H", "I"), 5 : ("J", "K", "L"), 6 : ("M", "N", "O"),\
         7 : ("P", "Q", "R", "S"), 8 : ("T", "U", "V"), 9 : ("W", "X", "Y", "Z")}
    if button == 1:
        return text[1]
    else:
        return text[button][num]

def main(quan):
    """SMS"""
    message = []
    for _ in range(quan):
        button = int(input())
        num = int(input())
        if text(button, num) == "del":
            message = message[:-(num)]
        else:
            message += text(button, num)
    if len(message) == 0:
        print("null")
    else:
        print("".join(message))
main(int(input()))
