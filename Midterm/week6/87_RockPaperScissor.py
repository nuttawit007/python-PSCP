"""Week 6""" #***
def rps(text):
    """RockPaperScissor"""
    score_a, score_b, _count, stock = 0, 0, 0, ""
    for letter in text:
        if _count < 2:
            _count += 1
            stock += letter
            if stock == "RS" or stock == "SP" or stock == "PR":
                score_a += 1
            elif stock == "SR" or stock == "PS" or stock == "RP":
                score_b += 1
            elif stock == "SS" or stock == "PP" or stock == "RR":
                pass
        if _count == 2:
            _count = 0
            stock = ""
    if score_a > score_b:
        print("A win %d-%d" % (score_a, score_b))
    elif score_b > score_a:
        print("B win %d-%d" % (score_b, score_a))
    else:
        print("DRAW", score_a)
rps(input())

'''RockPaperScissor'''
def rockpaper(fightlog):
    '''RockPaperScissor'''
    score_a = 0
    score_b = 0
    winningcase = ["RS", "PR", "SP"]
    for i in range(len(fightlog)//2):
        pairs = fightlog[2*i:(2*i)+2]
        if pairs[0] == pairs[1]: # กรณีเสมอ
            continue
        if pairs in winningcase:
            score_a += 1
        else:
            score_b += 1
    if score_a > score_b:
        print("A win %d-%d"%(score_a, score_b))
    elif score_b > score_a:
        print("B win %d-%d"%(score_b, score_a))
    else:
        print("DRAW %d"%(score_a))
rockpaper(input())
