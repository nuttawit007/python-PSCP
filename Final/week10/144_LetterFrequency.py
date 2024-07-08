"""Week10"""
def main():
    """LetterFrequency"""
    text = input().replace(" ", "")
    most_use, most_count = "", 0
    for letter in text:
        if letter.isalpha() == False:
            continue
        if letter.isupper():
            new_count = text.count("%s"%letter) + text.count("%s"%letter.lower())
        elif letter.islower():
            new_count = text.count("%s"%letter) + text.count("%s"%letter.upper())
        if new_count > most_count:
            most_count = new_count
            most_use = ""
            most_use += letter.lower()
    print(most_use)
main()
