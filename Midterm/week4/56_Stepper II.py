"""Week 4""" #***
def main(start, last):
    """Stepper II"""
    if start >= last:
        #print >> ถอยหลัง
        for _ in range(start, last-1, -1):
            print(_)
    else: 
        #print >> ไปข้างหน้า
        for _ in range(start, last+1):
            print(_)
main(int(input()), int(input()))
