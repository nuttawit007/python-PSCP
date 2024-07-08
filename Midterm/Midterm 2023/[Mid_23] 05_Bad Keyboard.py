"""[Midterm 2023] Bad Keyboard"""
def badkeyboard(text):
    """[Midterm 2023] Bad Keyboard"""
    new_text = ""
    for char in text:
        if char == "i":
            new_text += "o"
        elif char == "o":
            new_text += "i"
        elif char == "I":
            new_text += "O"
        elif char == "O":
            new_text += "I"
        else:
            new_text += char
    print(new_text)
badkeyboard(input())
