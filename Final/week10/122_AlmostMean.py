"""Week10"""
def main(quan):
    """Almostmean"""
    all_std = {}
    for _ in range(quan):
        data = input().split("\t")
        # เก็บข้อมูลเข้า dict >> ชื่อdict[key] = value
        all_std[data[0]] = float(data[1])
    total_score = 0
    for val in all_std.values():
        total_score += val
    mean = total_score/quan
    near_mean = max([val for val in all_std.values() if val < mean])
    # loop เข้าถึง key,val ใน dict
    for key, val in all_std.items(): 
        if val == near_mean:
            print(key+"\t"+str(val))
            break
main(int(input()))

""" อันเก่า """
# def main(quantity):
#     """AlmostMean"""
#     data = [input().split("\t") for _ in range(quantity)]
#     total_score = 0
#     for score in data:
#         total_score += float(score[1])
#     mean = total_score/quantity
#     less_mean = [score for score in data if float(score[1]) < mean]
#     near_mean = [less_mean[0]]
#     for score in less_mean:
#         if float(score[1]) > float(near_mean[0][1]):
#             near_mean[0] = score
#     print(near_mean[0][0]+"\t"+near_mean[0][1])
# main(int(input()))

