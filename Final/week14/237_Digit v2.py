"""Week 15"""
def main():
    """Digit v2"""
    num_text = input()
    unit = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    ten_nineteen = {"ten" : 10, "eleven" : 11, "twelve" : 12, "thirteen" : 13, "fourteen" : 14, "fifteen" : 15, "sixteen" : 16, "seventeen" : 17, "eighteen" : 18, "nineteen" : 19}
    _ty = {"twenty" : 20, "thirty" : 30, "fourty" : 40, "fifty" : 50, "sixty" : 60, "seventy" : 70, "eighty" : 80, "ninety" : 90}
    hun_thou = {"hundred" : 100, "thousand" : 1000}
    if "thousand" in num_text:
        pass
