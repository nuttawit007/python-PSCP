"""Week10"""
def myfunc(tuple_val):
    """Function for sorted: num1+num2 , num2 high"""
    # return  -int เพราะ เมื่อ sort จะไปอยู่ด้านหน้าสุด
    return int(tuple_val[0]) + int(tuple_val[1]), -int(tuple_val[1])

def main(amount):
    """Point Sorting"""
    for _ in range(amount):
        set_num = int(input())
        num_list = [input().split() for _ in range(set_num)]
        # เก็บค่าเป็น tuple ใน List
        data_list = [tuple(data) for data in num_list]
        print(data_list)
        sort_num = sorted(data_list, key=myfunc)
        for num in sort_num:
            print(num[0], num[1])
main(int(input()))
