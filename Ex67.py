s=0
while True:
    n=input("Tuoi: ")
    if not n:
        break
    else:
        t=int(n)
        if t<3:
            s=s+0
        elif 3<=t<=12:
            s=s+14
        elif t>65:
            s=s+18
        else:
            s=s+23
print("So tien phai tra la: ",s,".00$",sep="")        