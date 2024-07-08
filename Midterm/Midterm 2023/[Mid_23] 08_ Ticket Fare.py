"""[Midterm 2023] Ticket Fare"""
def main():
    """[Midterm 2023] Ticket Fare"""
    var_n = int(input())
    var_a = int(input())
    var_b = int(input())
    var_c = int(input())
    var_d = int(input())
    var_e = int(input())
    var_f = int(input())
    var_g = int(input())
    payment = 0
    count_station = abs(var_f - var_g)
    if count_station <= var_a:
        payment += var_b
    elif var_a < count_station <= (var_a+var_c):
        payment += var_b + ((count_station-var_a)*var_d)
    elif count_station > var_c:
        payment += var_b + (var_c*var_d) + ((count_station-(var_a+var_c))*var_e)
    if var_f > var_n or var_g > var_n:
        print("Error")
    else:
        print(payment)
main()
