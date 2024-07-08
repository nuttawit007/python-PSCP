"""Week 10""" #**
def main():
    """RemoveTag"""
    word = input()
    tag = ""
    remove = False #switch True/False
    for cha in word:
        # เมื่อเจอ tag ให้เริ่มต้นเข้าสู่การลบ
        if cha == "<":
            remove = True
        elif cha == ">":
            remove = False
            tag += cha
            word = word.replace(tag, " ") #replace tag ออก
            tag = ""
        # ตัวอักษรที่อยู่ภายใน tag
        if remove == True:
            tag += cha
    print(word.split())
main()

"""
Concept :ใช้ True/False เป็น switch ในการลบ tag ออก
"""
