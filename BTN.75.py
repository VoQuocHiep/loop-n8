def uocchunglonnhat(n, m):
    d = min(m, n)

    while m % d != 0 or n % d != 0:
       
        d -= 1
        return d
n = int(input("Nhap so nguyen dau tien: "))
m = int(input("Nhap so nguyen thu hai: "))
giatri = uocchunglonnhat(n, m)
print("Uoc chung lon nhat cua", n, "and", m, "is", giatri)