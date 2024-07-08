"""Timing II"""
def main(time):
    """Timing II"""
    second = time
    minute = second//60
    second = second%60
    hour = minute//60
    minute = minute%60
    day = hour//24
    hour = hour%24
    if day > 9999:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d"%(day, hour, minute, second))
main(int(input()))
