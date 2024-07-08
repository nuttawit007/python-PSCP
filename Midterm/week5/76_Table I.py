"""Week 5"""
def table(num):
    """Table I"""
    for _ in range(1, num+1):
        print("15 x %d = %d" % (_, _*15))
table(int(input()))
