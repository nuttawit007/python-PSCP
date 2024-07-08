"""Week 7""" #***
def main(_round):
    """[Midterm 2020] One For All"""
    if _round == 0:
        pass
    else:
        name = [input() for _ in range(_round)]
        for gen in range(1, len(name)+1):
            if gen == _round:
                print(name[gen-1], end="")
            elif gen % 2 != 0:
                print(name[gen-1] + "*"*gen, end="")
            else:
                print(name[gen-1] + "-"*gen, end="")
        print("_%d" % _round)
main(int(input()))
