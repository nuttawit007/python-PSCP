"""Week 3"""
def main(small_brick, big_brick, bride):
    """Brick Bridge"""
    big_use = bride // 5
    small_use = 0
    if big_brick >= big_use:
        small_use = bride - (big_use*5)
    elif big_brick < big_use:
        small_use = bride - (big_brick*5)
    if small_brick < small_use:
        print(-1)
    elif small_brick >= small_use:
        print(small_use)
main(int(input()), int(input()), int(input()))

'''Brick Bridge''' #162 ภูมิ
def brick(var_a, var_b, goal):
    '''Brick Bridge'''
    bigneed = min(goal//5, var_b)
    goal -= 5*bigneed
    if var_a < goal:
        print(-1)
    else:
        print(goal)
brick(int(input()), int(input()), int(input()))