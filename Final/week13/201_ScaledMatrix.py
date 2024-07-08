"""Week 13"""
def main(rows, columns):
    """ScaledMatrix"""
    # input ใส่ list แบบ matrix
    matrix = [[float(input()) for _ in range(columns)] for _ in range(rows)]
    # หาค่า max/min ใน list แบบ matrix
    max_val = max(max(row) for row in matrix)
    min_val = min(min(row) for row in matrix)
    for row in range(rows):
        for col in range(columns):
            """ scaled >> อัตราส่วน
                ค่าที่ต้องการ - ค่าที่น้อยสุด
                ____________________
                ค่าที่มากสุด - ค่าที่น้อยสุด
            """
            scaled = (matrix[row][col] - min_val) / (max_val - min_val)
            print("%.2f" % scaled, end=" ")
        print()
main(int(input()), int(input()))
