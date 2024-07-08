"""Week 11"""
def main(move, text):
    """CaesarV1"""
    new_text = ""
    for cha in text:
        # base คือ ตัว A/a แล้วหาว่าต้องขยับเท่าไหร่
        if cha.isalpha():
            if cha.isupper():
                diff = ord(cha) - ord("A")
                # % 26 เพื่อครอบคลุมทั้งการเลื่อนถอยหลังหรือขึ้นหน้า
                """ research >> 25+65 = 90("Z") 
                    %26 >> หารเอาเศษ
                """
                change = (diff + move) % 26
                new_text += chr(change + ord("A"))
            elif cha.islower():
                diff = ord(cha) - ord("a")
                change = (diff + move) % 26
                new_text += chr(change + ord("a"))
        else:
            new_text += cha
    print(new_text)
main(int(input()), input())

