def power(b,e):
    if e == 0:
        return 1
    elif e==1:
        return b
    else:
        return b*power(b,e-1)
b=int(input("Enter the base number:"))
e=int(input("Enter the exponent number:"))
result=power(b,e)
print(result)
