# """Week 7"""
# def main():
#     """[Midterm 2022] Palindrome"""
#     n_value = int(input())
#     value = input()
#     increment = 0
#     while increment != n_value:
#         x_value = "%02d" % (int(value[-2:]) + 1)
#         hours = value[0:2].replace(":", "")
#         if int(x_value) % 60 == 0 and int(x_value) != 0:
#             x_value = "00"
#             y_value = int(hours) + 1
#             hours = str(y_value)
#         if int(hours) % 24 == 0:
#             hours = "0"
#         value = hours + ":" + x_value
#         if value.replace(":", "") == value.replace(":", "")[::-1]:
#             increment = increment + 1
#             print(value)
# main()

'''[Midterm 2022] Palindrome'''
def findpalindome(findntime, time):
    '''[Midterm 2022] Palindrome'''
    hour = int(time[:time.index(":")])
    miute = int(time[time.index(":")+1:])
    start = hour*60 + miute + 1
    found = 0
    while True:
        if found == findntime:
            break
        hour = (start//60)%24
        miute = start%60
        text = "%d%02d"%(hour, miute)
        if text == text[::-1]:
            print("%d:%02d"%(hour, miute))
            found += 1
        start += 1
findpalindome(int(input()), input())