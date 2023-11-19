n = input("Nhập số nhị phân: ")
s=str(n)
decimal = 0
power = len(s) - 1  
for digit in s:
 decimal += int(digit) * (2 ** power)
 power -= 1
print(f"Số thập phân tương ứng là: {decimal}")
