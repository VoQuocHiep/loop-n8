import random
S = random.randint(1, 100)
d= 0
print(f"{S}")

for i in range(99):
    z = random.randint(1, 100)
    print(f"{z}",end="")
    
    if z > S:
        S= z
        d += 1
        print(" <== Update")
    else:
        print()

# Hiển thị kết quả cuối cùng
print(f"\nThe maximum value found was {S}")
print(f"The maximum value was updated {d}")
