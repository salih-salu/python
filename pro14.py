def facto(n):
    if(n<=1):
        return 1
    else:
        return n*facto(n-1)
number=input("Enter the number:")
print(facto(number))
