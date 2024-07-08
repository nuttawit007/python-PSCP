"""week 10"""
def main():
    """Classify"""
    person = []
    while True:
        std_id = input()
        if std_id == "END":
            break
        person.append(std_id[:4])
    same = ""
    for item in sorted(set(person)):
        year = item[:2]
        if year not in same:
            print(year, int(item[2:]), person.count(item))
        else:
            print("--", int(item[2:]), person.count(item))
        same = year
main()
