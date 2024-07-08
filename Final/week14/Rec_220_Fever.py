"""Week14"""
def main(temp):
    """fever"""
    if temp >= 40:
        print("Very High Fever")
    elif 39 <= temp < 40:
        print("High Fever")
    elif 38 <= temp < 39:
        print("Mild Fever")
    elif 36 <= temp < 38:
        print("No Fever")
main(float(input()))
