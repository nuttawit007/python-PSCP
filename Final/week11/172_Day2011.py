"""Week 11"""
def whatday(num):
    """Day2011"""
    dict_day = {1 : "Saturday", 2 : "Sunday", 3 : "Monday", 4 : "Tuesday",\
             5 : "Wednesday", 6 : "Thursday", 0 : "Friday"}
    return dict_day[num%7]

def main(day, month):
    """Day2011"""
    dict_month = {1 : 0, 2 : 31, 3 : 59, 4 : 90, 5 : 120, 6 : 151,\
            7 : 181, 8 : 212, 9 : 243, 10 : 273, 11 : 304, 12 : 334}
    day_in_year = day + dict_month[month]
    print(whatday(day_in_year))
main(int(input()), int(input()))
