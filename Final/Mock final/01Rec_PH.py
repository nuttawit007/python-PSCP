"""Mock final"""
def main(_ph):
    """PH"""
    if 7 < _ph <= 14:
        print("akaline")
    elif _ph == 7:
        print("neutral")
    elif 0 <= _ph < 7:
        print("acidic")
    else:
        print("error")
main(float(input()))
