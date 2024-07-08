"""[Midterm 2023] Niwarn World"""
import math
def eqa_x(var_n):
    """Equation eqa_x"""
    return 2 + ((math.log2(var_n**2))/(2*var_n*math.log2(var_n)))

def eqa_y(var_n, var_s):
    """Equation eqa_y"""
    return (math.sin(math.radians(30))+math.sqrt(2*var_s))/(eqa_x(var_n)+3)

def eqa_z(var_k):
    """Equation eqa_z"""
    return (eqa_y(var_k, var_k))**2 + (8456*(eqa_x(var_k))**4)/(24*var_k)

def main(var_n, var_s, var_k):
    """Result"""
    print("X: %.1f, Y: %.1f, Z: %.1f" % (eqa_x(var_n), eqa_y(var_n, var_s), eqa_z(var_k)))
main(float(input()), float(input()), float(input()))
