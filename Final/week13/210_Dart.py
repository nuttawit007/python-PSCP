"""Week 13"""
import math
def main(quan):
    """Dart"""
    score = 0
    for _ in range(quan):
        point = input().split()
        distance = math.sqrt((int(point[0])-0)**2 + (int(point[1])-0)**2)
        if distance > 10:
            score += 0
        elif 8 < distance <= 10:
            score += 1
        elif 6 < distance <= 8:
            score += 2
        elif 4 < distance <= 6:
            score += 3
        elif 2 < distance <= 4:
            score += 4
        elif 0 <= distance <= 2:
            score += 5
    print(score)
main(int(input()))
