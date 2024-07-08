"""Week 10"""
def main():
    """Muddled Menu"""
    ans = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        elif menu == "CLOSED":
            ans = []
            # return print >> จำทำให้ print บรรทัดล่างสุดไม่ทำงาน ถ้าเข้าเงื่อนไขนี้
            return print("Full Course: "+str(ans)+" Reversed: "+str(ans))
        elif menu[0:10] == "Can't do: ":
            ans.remove(menu[10:])
        elif menu == "SOMETHING'S WRONG":
            ans.clear()
            continue
        else:
            menu = menu.split(" #")
            # insert() >> เพื่อให้ยัดไปใน ตน ที่ถูกเลยทันที
            if menu[1].isnumeric():
                ans.insert(int(menu[1])-1, menu[0])
            else:
                ans.append(menu[0])
    print("Full Course: "+str(ans)+" Reversed: "+str(ans[::-1]))
main()


def main():
    """Muddle"""
    course = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        if menu == "CLOSED":
            course = []
            return print("Full Course:", course, "Reversed:", course)
        if menu[0:10] == "Can't do: ":
            course.remove(menu[10:])
        elif menu == "SOMETHING'S WRONG":
            course.clear()
            continue
        else:
            menu = menu.split(" #")
            if menu[1].isdigit():
                course.insert(int(menu[1])-1, menu[0])
            else:
                course.append(menu[0])
    print("Full Course:", course, "Reversed:", course[::-1])
main()
