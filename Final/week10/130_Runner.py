"""Week 10"""
def time(tuple_val):
    """find winner low time"""
    return (tuple_val[-1] - int(tuple_val[1])) / int(tuple_val[0]), -int(tuple_val[0])

def main(distance, quantity):
    """Runner"""
    num_list = [input().split() for _ in range(quantity)]
    # add distance in list
    num_dis_list = []
    for num in num_list:
        num.append(distance)
        num_dis_list.append(num)
    # change list to tuple
    data_list = [tuple(data) for data in num_list]
    sort_num = sorted(data_list, key=time)
    print(data_list.index(sort_num[0])+1)
main(int(input()), int(input()))
