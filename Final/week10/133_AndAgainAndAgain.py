"""Week10"""
def check_vowel(word):
    """check 2 vowel up"""
    vowel = "aeiou"
    vowel_count = 0
    for char in word:
        if char in vowel:
            vowel_count += 1
            if vowel_count >= 2:
                return True
def main():
    """AndAgain"""
    sentence = input().replace(".", " ").split()
    two_letter = [word for word in sentence if check_vowel(word)]
    dictionary_sort = sorted(two_letter)
    if len(dictionary_sort) != 0:
        for word in dictionary_sort:
            print(word)
    else:
        print("Nope")
main()
