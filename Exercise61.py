n=float(input(""))
s=0
i=1
if n==0:
    print("Loi")
while True:
    s=s+n
    tbc=s/i
    i=i+1
    n=float(input(""))
    if n==0:
        break
print(tbc)
    
