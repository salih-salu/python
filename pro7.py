lower = (int(input("Enter the lower limit:")))
upper = (int(input("Enter the upper limit:")))
print("The prime number in between", lower, "&", upper, "are:")
for n in range(lower, upper + 1):
    if n > 1:
        flag = 0
        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break
        if flag == 0:
            print(n)
