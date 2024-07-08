"""Week 11"""
def main():
    """Safe"""
    want = list(input())
    lock = list(input())
    spin = 0
    for let in range(len(lock)):
        if ord(want[let]) > ord(lock[let]):
            spin += min(ord(want[let])-ord(lock[let]), (90-ord(want[let]))+(ord(lock[let])-64))
        elif ord(want[let]) < ord(lock[let]):
            spin += min((90-ord(lock[let])) + (ord(want[let])-64), ord(lock[let])-ord(want[let]))
        else:
            spin += 0
    print(spin)
main()
