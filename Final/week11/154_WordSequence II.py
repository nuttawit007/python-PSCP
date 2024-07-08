"""Week 11"""
def main(word1, word2):
    """WordSequence II"""
    for cha in range(max(len(word1), len(word2))+1):
        print(word2[:cha] + word1[cha:])
main(input(), input())
