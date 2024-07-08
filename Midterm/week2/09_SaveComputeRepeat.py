"""SaveComputeRepeat"""
def main():
    """SaveComputeRepeat"""
    start = int(input())
    milliseconds = start
    seconds = milliseconds//1000
    milliseconds = milliseconds%1000
    minutes = seconds//60
    seconds = seconds%60
    hour = minutes//60
    minutes = minutes%60
    day = hour//24
    hour = hour%24
    print(day, hour, minutes, seconds, milliseconds)
main()

"""การคิดอีกรูปแบบนึง เริ่มจากหน่วยเวลามากสุด"""
def main(second):
    day = second//86400
    second = second%86400
    hours = second//3600
    second = second%3600
    minute = second//60
    second = second%60
    print(day, hours, minute, second)
main(int(input()))