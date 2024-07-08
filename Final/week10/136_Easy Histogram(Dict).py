"""Week 10"""
def smallbforebig(char):
    """Use ascii to check letter"""
    if ord(char) <= 90:
        return ord(char) + 32.5
    return ord(char)

def main(text):
    """Use dict for count how many letter in text"""
    dict_text = {}
    for letter in text:
        dict_text[letter] = dict_text.get(letter, 0) + 1
    key_text = [key for key in dict_text]
    sort_letter = sorted(key_text, key=smallbforebig)
    for letter in sort_letter:
        print(letter, "=", dict_text[letter])
main(input().replace(" ", ""))
