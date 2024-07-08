"""Week 5""" #***
def grade(subject):
    """Grade III"""
    all_grade = 0
    for _ in range(subject):
        score = float(input())
        if 95 <= score <= 100:
            all_grade += 4
        elif score >= 90:
            all_grade += 3.5
        elif score >= 85:
            all_grade += 3
        elif score >= 80:
            all_grade += 2.5
        elif score >= 75:
            all_grade += 2
        elif score >= 70:
            all_grade += 1.5
        elif score >= 65:
            all_grade += 1
        elif score >= 60:
            all_grade += 0.5
        elif score >= 0:
            all_grade += 0
    gpa = int((all_grade/subject)*100)/100
    print("%.2f" % gpa)
grade(int(input()))
