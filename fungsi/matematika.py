import math

def PersamanKuadrat(a: float | int, b: float | int, c: float | int) -> float:
    """
    mencari sebuah x 
    misal ax^2+bx+c
    a : nilai variable pertama
    b : nilai variable kedua
    c : nilai constanta
    """
    return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a), (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

# print(PersamanKuadrat(a, b, c))
x1, x2 = PersamanKuadrat(2, -5, -3)
print(f"Nilai x: {x1} dan Nilai x: {x2}")



def persamaanGarisLurus(x: float | int, y: float | int) -> float:
    """
    x - x1
    """





