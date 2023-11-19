x=xx=float(input("Enter the x part of the coordinate: "))
y=yy=float(input("Enter the y part of the coordinate: "))
cv=0
while True:
    x2=(input("Enter the x part of the coordinate: (blank to quit): "))
    if not x2:
        if cv==0 or cv==canh:
            print("Nhap it nhat 3 diem")
            break
        else:
            a=x22-xx
            b=y22-yy
            import math
            canh=math.sqrt(a**2+b**2)
            cv=cv+canh
            print(cv)
            break
    y2=(input("Enter the y part of the coordinate: "))
    x22=float(x2)
    y22=float(y2)
    a=x22-x
    b=y22-y
    import math
    canh=math.sqrt(a**2+b**2)
    cv=cv+canh
    x=x22
    y=y22
