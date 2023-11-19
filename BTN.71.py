import math

def newton_sqrt(x):
    doan = x / 2

    while abs(doan * doan - x) > 0.000000000001:
        doan = (doan + x / doan) / 2
    return doan
x = float(input("Nhap mot so: "))
canbachai = newton_sqrt(x)
print("Can bac hai:", canbachai)
print("Kiemtra:", math.sqrt(x) == canbachai)