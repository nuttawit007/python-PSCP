"""Week 15"""
def range_kid(wpm):
    """Range(WPM) for kid"""
    if wpm > 40:
        return "Very Fast"
    elif 31 <= wpm <= 40:
        return "Fast"
    elif 21 <= wpm <= 30:
        return "Average"
    elif 11 <= wpm <= 20:
        return "Slow"
    elif wpm < 11:
        return "Very Slow"

def range_adult(wpm):
    """Range(WPM) for adult"""
    if wpm > 80:
        return "Insane"
    elif 66 <= wpm <= 80:
        return "Very Fast"
    elif 46 <= wpm <= 65:
        return "Fast/Advanced"
    elif 36 <= wpm <= 45:
        return "Intermediate/Average"
    elif 26 <= wpm <= 35:
        return "Slow/Beginner"
    elif wpm < 26:
        return "Very Slow"

def main(gen, wpm):
    """WPM"""
    if gen == "Kids":
        print(range_kid(wpm))
    elif gen == "Adults":
        print(range_adult(wpm))
main(input(), int(input()))
