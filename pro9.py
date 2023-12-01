num = (int(input("enter the number to check perfect or not:")))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print("The number", num, "is a perfect number")
else:
    print("The number", num, "is not a perfect number")
