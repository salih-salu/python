def bi_to_dec(n):
    decimal=0
    power=1
    while(n>0):
        rem=n%10
        n=n//10
        decimal=decimal+(rem*power)
        power=power*2
    return decimal
binary=int(input("Enter the binary number:"))
print("the decimal value is :",bi_to_dec(binary))
