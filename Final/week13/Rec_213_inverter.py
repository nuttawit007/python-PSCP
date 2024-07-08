"""Week 13"""
def main():
    """Inverter"""
    bit = input()
    new_bit = ''
    for _ in bit:
        if _ == "1":
            new_bit += "0"
        elif _ == "0":
            new_bit += "1"
    print(new_bit.lstrip("0"))
main()
