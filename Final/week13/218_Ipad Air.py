"""Week 13"""
def main(color, store, wifi):
    """IpadAir"""
    color_list = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    if color in color_list and wifi == "Wi-Fi" and store == "64":
        print(19900)
    elif color in color_list and wifi == "Wi-Fi" and store == "256":
        print(24900)
    elif color in color_list and wifi == "Wi-Fi + Cellular" and store == "64":
        print(24400)
    elif color in color_list and wifi == "Wi-Fi + Cellular" and store == "256":
        print(29400)
    else:
        print("Not Available")
main(input(), input(), input())
