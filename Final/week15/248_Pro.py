"""Week 15"""
def main(come, pay, price, people):
    """Pro"""
    # จำนวน pro
    can_pro = people//come
    # จน คนกินฟรี
    free_people = can_pro*(come-pay)
    payment = price*(people-free_people)
    print(payment)
main(int(input()), int(input()), int(input()), int(input()))
