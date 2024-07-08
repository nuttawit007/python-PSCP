"""Week 10"""
def main(quan):
    """Cutecat Cutefox"""
    only_cat, only_fox, catfox = {}, {}, {}
    # รับ string >> เก็บเป็น dict
    for _ in range(quan):
        pet = input().strip("{}").replace("\"", "").split(" : ")
        # strip("\'") กรณี single code ออก >> {'Chiba' : 'Cat01'}
        if "Fox" in pet[1]:
            only_fox.update({pet[0].strip("\'"):pet[1].strip("\'")})
        elif "Cat" in pet[1]:
            only_cat.update({pet[0].strip("\'"):pet[1].strip("\'")})
        catfox.update({pet[0].strip("\'"):pet[1].strip("\'")})
    # update >> ถ้าไม่มี Garfield / Fubuki ให้เพิ่มเข้าไป
    if "Cat01" not in catfox.values() and "Garfield" not in catfox.keys():
        only_cat.update({"Garfield":"Cat01"})
    if "Fox01" not in catfox.values() and "Fubuki" not in catfox.keys():
        only_fox.update({"Fubuki":"Fox01"})
    # sort ค่า value cat/fox
    sorted_cat = dict(sorted(only_cat.items(), key=lambda item: int(item[1][3:])))
    sorted_fox = dict(sorted(only_fox.items(), key=lambda item: int(item[1][3:])))
    # Output
    print("Cat :", len(only_cat))
    print("Fox :", len(only_fox))
    for key in sorted_cat.keys():
        print(key, ":", only_cat[key])
    for key in sorted_fox.keys():
        print(key, ":", only_fox[key])
main(int(input()))
