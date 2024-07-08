"""Week 6"""
def near(alice, bob, ice):
    """Near ice"""
    near_alice = abs(ice - alice)
    near_bob = abs(ice - bob)
    if near_alice > near_bob:
        print("Bob", near_bob)
    elif near_bob > near_alice:
        print("Alice", near_alice)
    else:
        print("Sundaes", near_alice)
near(int(input()), int(input()), int(input()))

