"""week 16"""
def main(quan):
    """MusicLover"""
    dic_music = {}
    for _ in range(quan):
        music = input().split("-")
        # การกำหนดชื่อตัวแปรของค่าใน list
        name, song = music
        # การเพิ่มค่าใน dic รูปแบบ {"key1" : ["val1", "val2"]}
        if name in dic_music:
            # กรณีมี key อยู่แล้วให้ทำการเพิ่มค่าเข้าไปแทน >> สามารถใช้ append และ extend
            # เก็บค่า val แบบ list
            dic_music[name].append(song)
        else:
            # ถ้ายังไม่มี key ให้เพิ่มค่าใหม่
            dic_music[name] = [song] # ใส่ [] ครอบค่า val เพื่อให้เป็น list ในค่าเรื่มต้น
    # การแสดงผล
    for key, val in dic_music.items():
        print(key)
        # loop ชื่อเพลงทั้งหมดที่อยู่ใน list
        for music in val:
            print(music)
main(int(input()))
