"""Week 6"""
def christmastree(leaf, stem):
    """Christmastree"""
    for i in range(1, leaf + 1):
        print(" " * (leaf - i) + "*" * (2 * i - 1))
    for _ in range(stem):
        print(" " * (leaf-2) + "---")
christmastree(int(input()), int(input()))
