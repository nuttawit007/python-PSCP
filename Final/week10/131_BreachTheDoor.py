"""Week10"""
def main():
    """BreachTheDoor"""
    text = input().split()
    six_letter = []
    for word in text:
        if len(word) > 6:
            if word.isalpha() == False:
                alphabet = ""
                for item in word:
                    if item.isalpha():
                        alphabet += item
                if len(alphabet) > 6:
                    six_letter.append(alphabet)
            else:
                six_letter.append(word)
    for word in six_letter:
        print(word, end=" ")
main()
