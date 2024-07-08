"""Week 11"""
def main(num):
    """OneTwo same fibonacci"""
    if num <= 2:
        return "%s" % num
    else:
        return "%s" % (main(num-1) + main(num-2))
print(main(int(input())))
