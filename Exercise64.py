s=0
while True:
    t=(input(""))
    if not t:
        break
    m=float(t)
    s=s+m
print("Tong so tien:",s)
if s%5<2.5:
    s=s-(s%5)
else:
    s=s-(s%5)+5
print("Phai tra:",s)
