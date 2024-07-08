"""Week 13"""
def main(var_p, var_q, var_r):
    """MultiplyMatrixPQR"""
    matrix_a = [[int(input()) for _ in range(var_q)]for _ in range(var_p)]
    matrix_b = [[int(input()) for _ in range(var_r)]for _ in range(var_q)]
    for row in range(var_p):
        for col in range(var_r):
            values = 0
            for val in range(var_q):
                values += matrix_a[row][val]*matrix_b[val][col]
            print(values, end=" ")
        print()
main(int(input()), int(input()), int(input()))
