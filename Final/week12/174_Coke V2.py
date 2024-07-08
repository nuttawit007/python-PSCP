"""Week 12"""
def coke(normal, lid, special, bottle):
    """Coke V2"""
    no_discount = normal * bottle
    if bottle > 0 and normal > special and lid > 0:
        discount_amount = (bottle - 1) // lid
        discount_cost = discount_amount * (normal - special)
        print(no_discount - discount_cost)
    else:
        print(no_discount)
coke(int(input()), int(input()), int(input()), int(input()))
