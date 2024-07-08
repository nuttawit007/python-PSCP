"""Week 11"""
def main(high):
    """Divide3Or5"""
    score = 0
    for num in range(1, high+1):
        if num%3 == 0 or num%5 == 0:
            score += num
    print(score)
main(int(input()))
