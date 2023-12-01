def sumn(n):
    sum = 0
    for i in range(1,1+n):
        sum+=i
    return sum
print("Program to find the sum of first n numbers:")
num=(int(input("Enter the limit:")))
result = sumn(num)
print("sum is ",result)
