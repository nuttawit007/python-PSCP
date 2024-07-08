"""Week 11"""
def main():
    """ClockHands"""
    hour = int(input())
    minutes = int(input())
    hour *= 5 # มองเลขชั่วโมงเป็น นาทีนั้นๆ
    hour += minutes / 12 # จากอีกชั่งโมงไปอีกชั่วโมง ทุกๆนาทีเข็มก็จะขยับ
    hour %= 60 # ไม่เกิน 60 นาที
    print(minutes <= hour < minutes+1)
main()
