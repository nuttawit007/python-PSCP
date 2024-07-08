"""Week 3"""
def main(name, age):
    """Robot I"""
    if 0 < age < 18:
        print(name + ", you can pass.")
    else:
        print(name + ", you shall not pass.")
main(input(), float(input()))
