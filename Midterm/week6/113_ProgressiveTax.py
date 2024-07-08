"""Week 6"""
def main(salary):
    """ProgressiveTax"""
    total_tax = 0
    while salary > 150000:
        tax = 0
        if salary > 4000000:
            tax = (salary - 4000000)*0.35
            salary -= (salary - 4000000)
        elif 2000000 < salary <= 4000000:
            tax = (salary - 2000000)*0.3
            salary -= (salary - 2000000)
        elif 1000000 < salary <= 2000000:
            tax = (salary - 1000000)*0.25
            salary -= (salary - 1000000)
        elif 750000 < salary <= 1000000:
            tax = (salary - 750000)*0.2
            salary -= (salary - 750000)
        elif 500000 < salary <= 750000:
            tax = (salary - 500000)*0.15
            salary -= (salary - 500000)
        elif 300000 < salary <= 500000:
            tax = (salary - 300000)*0.1
            salary -= (salary - 300000)
        elif 150000 < salary <= 300000:
            tax = (salary - 150000)*0.05
            salary -= (salary - 150000)
        total_tax += tax
    print(int(total_tax))
main(int(input()))
