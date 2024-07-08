"""zip"""
name = ["win", "aom", "yam"]
age = [18, 20, 35]
z = zip(name, age) # เอาตัวแรกของ name กับ age มารวมกันเป็น tuple
print(list(z)) #[('a', 1), ('b', 2), ('c', 3)]

"""
ถ้าใช้ for กับ zip จะloop ได้แค่ 1 รอบเท่านั้น ไม่สามารถ for ซ้ำได้ ถ้าอยากใช้หลายรอบ ให้เก็บค่า zip ไว้ในตัวแปร
"""
for item in z:
    print(item)

"""enumerate >> enumerate(text, ลำดับที่จะเริ่มต้น)"""
s = "abc"
for a,b in enumerate(s):
    print(a, b)
    """
    0 a
    1 b
    2 c
    """

for a, b in enumerate(s, 1):
    print(a, b)
    """
    1 a
    2 b
    3 c
    """

"""isinstance >> check ว่า ข้อมูลเป็นแบบที่บอกมั้ย"""
print(isinstance([1, 2, 3], list))

