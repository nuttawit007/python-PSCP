"""Week 13"""
import math
def main(quan):
    """EuclideanDistance"""
    point = [[int(num) for num in input().split()]for _ in range(quan)]
    distance = 0
    for i in range(quan-1):
        distance += math.sqrt(((point[i+1][0]-point[i][0])**2)+((point[i+1][1]-point[i][1])**2))
    print("%.2f" % distance)
main(int(input()))
