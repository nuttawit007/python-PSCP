"""Week 3""" """ค่ามากสุดสามารถมีได้ 2 ค่า >> คนที่ 2 สามารถได้คะแนนเท่ากับคนที่ได้มากที่สุด"""
def main(score, high_score):
    """SurprisingVote"""
    if score - (high_score*2) < high_score-2 and high_score > 2: #high score*2 >> คิดว่า คนที่2ได้คะแนนเท่ากับคนสูงสุด
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()), float(input()))

def main(score, high_score): #จารโช
    second = min(score-high_score, high_score)
    low_score = score - high_score - second
    if high_score - low_score > 2:
        print("Surprising")
    else:
        print("Not surprising")
main(float(input()), float(input()))

def surprising(total, highest):#จารโช one line
    """Surprising"""
    return "Surprising" if 2*highest - total + min(total-highest, highest) > 2 else "Not surprising"
print(surprising(float(input()), float(input())))
