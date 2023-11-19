def palindrome(chuoi):
   
    chuoi = chuoi.lower().replace(" ", "")

    
    dodai = len(chuoi)
    for i in range(dodai // 2):
        if chuoi[i] != chuoi[dodai - 1 - i]:
            return False

    return True


chuoi = input("Nhap mot chuoi: ")

if palindrome(chuoi):
    print(chuoi, "la palindrome")
else:
    print(chuoi, "khong phai palindrome")