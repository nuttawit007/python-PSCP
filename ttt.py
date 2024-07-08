"""TicTacToe"""
def main():
    """main"""
    mylist = []
    for _ in range(3):
        txt = input()
        newlist = [i for i in txt]
        mylist.append(newlist)
    if (mylist[0][0] == mylist[1][1] == mylist[2][2] \
        or  mylist[0][2] == mylist[1][1] == mylist[2][0]) and mylist[1][1] != "-":
        return "%s WIN" % (mylist[1][1])
    for i in range(3):
        if mylist[i][0] == mylist[i][1] == mylist[i][2] and mylist[i][1] != "-":
            return "%s WIN" % (mylist[i][0])
    for i in range(3):
        if mylist[0][i] == mylist[1][i] == mylist[2][i] and mylist[1][i] != "-":
            return "%s WIN" % (mylist[0][i])
    return "DRAW"
print(main())
