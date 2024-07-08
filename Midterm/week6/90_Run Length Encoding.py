# """Week 6""" #***
# def main(coding):
#     """Run Length Encoding"""
#     tmp = coding[0]
#     roundword, stringword = 0, ""
#     for i in range(len(coding)):
#         if coding[i] == tmp:
#             roundword += 1
#         else:
#             stringword += str(roundword) + coding[i-1]
#             tmp = coding[i]
#             roundword = 1
#     stringword += str(roundword) + coding[-1]
#     print(stringword)
# main(input())

"""Run Length Encoding"""
def encode(message):
    """Encode a message"""
    last_letter = message[0]
    count = 0
    for letter in message:
        if letter != last_letter:
            print(str(count)+last_letter, end='')
            count = 1
        else:
            count += 1
        last_letter = letter
encode(input()+' ')