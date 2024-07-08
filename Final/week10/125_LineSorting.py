"""LineSorting"""
def main(num):
    """LineSorting"""
    lis_text = []
    for _ in range(num):
        text = input()
        lis_text.append(text)
    lis_text.sort(key=len)
    for text in lis_text:
        print(text)
main(int(input()))
