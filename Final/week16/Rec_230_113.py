"""week 16"""
def main():
    """113"""
    number = input().replace("113", "")
    while True:
        if "113" not in number:
            break
        else:
            number = number.replace("113", "")
    print(number)
main()
