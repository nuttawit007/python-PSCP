"""Final 02"""
def check_vowel(word):
    """check the last vowel"""
    vowels = ["a", "e", "i", "o", "u"]
    last_vowel = [cha for cha in word if cha in vowels]
    last_vowel = [] # e o
    if len(last_vowel) > 0:
        return last_vowel[-1]
    else:
        return last_vowel

def index_vowel(word):
    """return index"""
    vowels = ["a", "e", "i", "o", "u"]
    count, vowel_index = -1, 0
    for cha in word:
        count += 1
        if cha in vowels:
            vowel_index = count
    return vowel_index

def main(word):
    """Helloooo"""
    lis_word = list(word)
    if len(check_vowel(word)) != 0:
        lis_word.insert(index_vowel(word), check_vowel(word)*3)
        newword = "".join(lis_word)
        print(newword)
    else:
        print(word)
main(input())
