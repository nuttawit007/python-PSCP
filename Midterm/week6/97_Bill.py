"""Week 6"""
def bill(price):
    """bill"""
    service_charge = price * (10/100)
    if service_charge < 50:
        service_charge = 50
    elif service_charge > 1000:
        service_charge = 1000
    vat = (price + service_charge) * (7/100)
    total_price = price + service_charge + vat
    print("%.2f" % (total_price))
bill(int(input()))
