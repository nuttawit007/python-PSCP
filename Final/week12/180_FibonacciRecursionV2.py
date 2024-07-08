"""Week 12"""
def main(number, data):
    """Fibanacci 2"""
    if number in data:
        return data[number]
    if number <= 1:
        return number
    if number > 500:
        main(number-500, data)
    res = main(number-2, data) + main(number-1, data)
    data[number] = res
    return res

def mainn():
    """main"""
    data = {0:0, 1: 1}
    number = int(input())
    result = main(number, data)
    print(result)
mainn()
