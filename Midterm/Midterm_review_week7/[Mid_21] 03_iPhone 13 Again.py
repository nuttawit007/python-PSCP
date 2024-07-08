"""Week 7"""
def byte(memory):
    """price_gen"""
    if memory == "256 GB":
        return 4000
    elif memory == "512 GB":
        return 12000
    elif memory == "1 TB":
        return 20000
    else:
        return 0

def iphone13(iphone, memory):
    """[Midterm 2021] iPhone 13 Again"""
    low = "128 GB 256 GB 512 GB"
    high = "128 GB 256 GB 512 GB 1 TB"
    if iphone == "iPhone 13 mini" and memory in low:
        print(25900 + byte(memory))
    elif iphone == "iPhone 13" and memory in low:
        print(29900 + byte(memory))
    elif iphone == "iPhone 13 Pro" and memory in high:
        print(38900 + byte(memory))
    elif iphone == "iPhone 13 Pro Max" and memory in high:
        print(42900 + byte(memory))
    else:
        print("Not Available")
iphone13(input(), input())
