"""Week10"""
def main():
    """Filter"""
    all_std = input().strip("{}").replace("\"", "").replace(",", ":").split(": ")
    score = float(input())
    # แปลง list >> ใส่ dict
    std_score ={}
    for i in range(0, len(all_std)-1, 2):
        std_score.update({all_std[i]: float(all_std[i+1])})
    # filter คะแนนที่เกิน score ที่กำหนด
    """ append >> คนที่คะแนนเกินขั้นต่ำ"""
    filter_score = []
    for point in std_score:
        if std_score[point] >= score:
            filter_score.append(point)
    # Output
    """len(filter_score) >> ดูว่าใน dict มีค่าอยู่ในนั้นมั้ย"""
    if len(filter_score) == 0:
        print("Nope")
    else:
        for std in sorted(filter_score): # sorted ด้วย list ง่ายกว่า dict แล้วไปดึงค่าจาก dict
            print("%s\t%.2f" % (std, std_score[std]))
main()

""" Use JASON"""

"""Ejudge"""
import json
def main():
    """Filter"""
    """ jason.loads() การทำให้ dict ที่อยู่ในรูป str เป็น dict โดย auto """
    dictscore = json.loads(input()) 
    socre = float(input())
    ans = []
    for i in dictscore:
        if dictscore[i] >= socre:
            ans.append(i)
    if len(ans) == 0:
        print("Nope")
    else:
        for i in sorted(ans):
            print("%s\t%.2f"%(i, dictscore[i]))
main()