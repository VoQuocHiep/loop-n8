n = int(input("Enter an integer (2 or greater) : "))  
s=n     
if s < 2:
   print("Enter an integer greater than or equal to 2")
else:
    S=[]
    for factor in range(2, s + 1):
        while s % factor == 0:
            S.append(factor)
            s //= factor
    
    print(f"The prime factors of {n} are:")
    for factor in S:
     print(factor)
