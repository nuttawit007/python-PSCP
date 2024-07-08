# """Kayak"""
# def kayak(num, people):
#     """Kayak"""
#     weight = people.split(" ")
#     weight = [int(weight[_]) for _ in range(len(weight))] #เปลี่ยนชนิดข้อมูลใน list
#     if len(weight) == (2*num):
#         weight.remove(max(weight)) #ลบค่ามากสุดใน list
#         weight.remove(max(weight)) #ลบค่ามากสุดใน list
#     sort_wei = [_ for _ in sorted(weight)] #sort น้อยไปมาก
#     diff = [abs(sort_wei[i]-sort_wei[i+1]) for i in range(0, len(sort_wei), 2)] #จำนวนน้อยสุดมาลบกัน
#     sum_weight = 0
#     for i in diff: #เอาผลต่างมาบวกกัน
#         sum_weight = sum_weight + i
#     print(sum_weight)
# kayak(int(input()), input())

def kayak():
    """kayak"""
    num = int(input())
    weight = input().split(" ")
    total = 0
    for i in range(len(weight)): #เปลี่ยนเลขใน list จาก str >> int
        weight[i] = int(weight[i])
    weight.sort() #sort ตัวเลข
    for _ in range(num-1): #จำนวนเรือนั่ง 2 คน
        diff = [] #เก็บผลต่าง เลขมากกว่า-เลขน้อยกว่า
        for i in range(1, len(weight)):
            diff.append(weight[i]-weight[i-1])
        total += min(diff) #เอาค่าที่น้อยที่สุดที่ได้
        del_value = diff.index(min(diff)) #เอา index ตัวที่มีค่่าน้อยสุด
        del weight[del_value:del_value + 2] # ลบคนที่จะเอาไปนั่งเรือ 2 คนออก
    print(total)
kayak()

def kayak(num, weight, total=0):
    for _ in range(num-1):
        diff = [weight[i] - weight[i-1] for i in range(1, len(weight))]
        total += min(diff)
        del weight[diff.index(min(diff)):diff.index(min(diff))+2]
    print(total)
kayak(int(input()), sorted([int(i) for i in input().split(" ")]))
