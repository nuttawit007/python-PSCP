"""Week 7"""
import math
def high(num1, num2):
    """high num"""
    if num1 > num2:
        return num1
    else:
        return num2

def main(pushups, situps, looknang, run):
    """"[Midterm 2021] ฉันจะเป็น Saitama ให้ได้เลย"""
    can_push, can_sit, can_run, can_look = int(input()), int(input()), int(input()), int(input())
    amo_push = pushups/can_push
    amo_sit = situps/can_sit
    amo_look = looknang/can_look
    amo_run = run/can_run
    time_to_do = high(high(high(amo_push, amo_sit), amo_look), amo_run)
    print(math.ceil(time_to_do))
main(int(input()), int(input()), int(input()), int(input()))
