"""Week 3"""
def check_balance(avg, weight1, weight2, weight3, weight4):
    """over lenght"""
    _min, _max = avg/2, avg + (avg/2)
    if _min <= weight1 <= _max and _min <= weight2 <= _max and\
         _min <= weight3 <= _max and _min <= weight4 <= _max:
        return "balance"
    else:
        return "Unbalance"

def main(avg, weight1, weight2, weight3):
    """weightStation"""
    weight4 = (avg*4)-weight1-weight2-weight3
    total_weight = weight1+weight2+weight3+weight4
    balance = check_balance(avg, weight1, weight2, weight3, weight4)
    if total_weight > 15000 and balance == "Unbalance":
        print("Overweight")
    elif total_weight > 15000:
        print("Overweight")
    elif balance == "Unbalance":
        print("Unbalance")
    else:
        print("Pass %.2f" % weight4)
main(float(input()), float(input()), float(input()), float(input()))
