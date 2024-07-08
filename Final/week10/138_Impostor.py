"""Week10"""
def main():
    """Impostor"""
    all_member, out = {}, []
    # รับ string หน้าตาเหมือน dict >> เก็บเป็น dict
    # เก็บ member ทั้งหมด
    while True:
        member = input()
        if member == "Start":
            break
        member = member.strip("{}").replace("\"", "").split(" : ")
        all_member.update({member[0]:member[1]})
    # เก็บ คนคัดออก ทั้งหมด
    while True:
        color = input()
        if color == "End":
            break
        out.append(color)
    dead_member = {}
    for mem in out:
        dead_member.update({mem:all_member[mem]}) # dead member ทั้งหมด >> update เข้าไป
        all_member.pop(mem) # ลบ dead member ออกจาก all_member
    # Imposter ที่เหลือ
    check_impo = [all_member[mem] for mem in all_member if all_member[mem] == "Impostor"]
    # Output
    print(len(check_impo), "Impostor Remains")
    print("***Alive***")
    # การ print key,val ออกมา
    for key, val in sorted(all_member.items()): # sorted เรียงตามตัวอักษร(โจทย์บอก)
        print("{} : {}".format(key, val)) 
    print("***Dead***")
    for key, val in sorted(dead_member.items()):
        print("{} : {}".format(key, val))
main()

