"""Week 6"""
def main(_round):
    """ValidVar"""
    reserved_word = ["if", "else", "elif", "while", "for", "True", "False",\
     "continue", "break", "return", "is", "in", "and",\
     "or", "from", "as", "pass", "not", "def", "None"]
    for _ in range(_round):
        text = input()
        if text.isidentifier() and text not in reserved_word:
            print("Valid")
        else:
            print("Invalid")
main(int(input()))