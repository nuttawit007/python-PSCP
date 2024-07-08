"""Week 15"""
def main(text1, text2):
    """Hamming"""
    diff = 0
    for cha in range(len(text1)):
        if text1[cha] != text2[cha]:
            diff += 1
    print(diff)
main(list(input()), list(input()))
