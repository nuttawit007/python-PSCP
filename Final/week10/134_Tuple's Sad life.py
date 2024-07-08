"""Week10"""
def main():
    """Tuple's Sad life"""
    text = tuple(input().split())
    want = input()
    text_index = text.index("%s" % want)
    text_count = text.count("%s" % want)
    for _ in range(text_count):
        for _ in range(text_count):
            print("%s" % text_index, end=" ")
        print()
main()
