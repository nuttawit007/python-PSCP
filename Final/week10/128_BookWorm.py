"""Week 10"""
def main(_set):
    """BookWorm"""
    # จำนวนชุดทดสอบ
    for _ in range(_set):
        time, book = int(input()), int(input())
        # เวลาอ่านแต่ละเล่ม >> อ่านให้ได้มาสุด >> ต้อง sorted เพื่อให้อ่านเล่มที่ใช้เวลาน้อยๆก่อน
        time_per_book = sorted([float(input()) for _ in range(book)])
        # นับว่าอ่านได้มากสุดกี่เล่ม
        count = 0
        for tim in time_per_book:
            time -= tim
            if time >= 0:
                count += 1
        print(count)
main(int(input()))
