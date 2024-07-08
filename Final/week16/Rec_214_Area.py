"""Week 16"""
def main():
    """Area"""
    row = int(input())
    area = 0
    for _ in range(row):
        text = input()
        area += len(text) - text.count(" ")
    print(area)
main()
