import re

def palindrome(chuoi):
    caithienchuoi = re.sub(r"[^\w]", "", chuoi.lower())

    dodai = len(caithienchuoi)
    for i in range(dodai // 2):
        if caithienchuoi[i] != caithienchuoi[dodai - 1 - i]:
            return False

    return True

chuoi = input("Nhap mot chuoi: ")

if palindrome(chuoi):
    print(chuoi, "is a palindrome")
else:
    print(chuoi, "is not a palindrome")
