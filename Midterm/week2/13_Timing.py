"""Timing"""
def main(num):
    '''Main Function'''
    # Write your code here
    second = num
    mi_ute = second//60
    second = second%60
    hour = mi_ute//60
    mi_ute = mi_ute%60
    day = hour//24
    hour = hour%24
    print(day, "day", hour, "hours", mi_ute, "minutes", second, "second.")
main(int(input()))
