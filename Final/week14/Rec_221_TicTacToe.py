"""Week 14"""
def main():
    """TicTacToe"""
    table = [list(input()) for _ in range(3)]
    # แนวเฉียง
    if (table[0][0] == table[1][1] == table[2][2] or\
     table[0][2] == table[1][1] == table[2][0]) and table[1][1] != "-":
        return "%s WIN" % table[1][1]
    # แนวนอน
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] and table[i][1] != "-":
            return "%s WIN" % table[i][1]
    # แนวตั้ง
    for i in range(3):
        if table[0][i] == table[1][i] == table[2][i] and table[1][i] != "-":
            return "%s WIN" % table[1][i]
    return "DRAW"
print(main())
