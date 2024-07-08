"""Week 12"""
import hashlib
def main(password):
    """security password use import hashilb"""
    encode_byte = password.encode('utf-8') # แปลงข้อความเป็น byte
    sha_512_64bit = hashlib.sha512(encode_byte) # สร้าง object สำหรับ 64bit
    hex_number = sha_512_64bit.hexdigest() # แปลงเป็นเลขฐาน 16 128ตัว
    print(hex_number.upper())
main(input())
