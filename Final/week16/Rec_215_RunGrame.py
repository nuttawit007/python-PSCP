"""Week 16"""
def main():
    """RunGrame"""
    point = list(map(int, input().split()))
    if len(point) >= 1:
        distance = abs(point[0])
        for i in range(len(point) - 1):
            distance += abs(point[i] - point[i+1])
        print(distance)
    else:
        print(0)
main()
