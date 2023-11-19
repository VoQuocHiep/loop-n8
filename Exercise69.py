pi=3
a=2
b=3
c=4
while a<1000000:
    pi=pi+(4/(a*b*c))-(4/((a+2)*(b+2)*(c+2)))
    a=a+4
    b=b+4
    c=c+4
print(round(pi,15))
