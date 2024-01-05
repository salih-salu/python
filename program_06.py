num = int(input("Enter the number : "))
lim = int(input("Enter the Limit : "))
print("Multiplication table of ", num, " is ")
i = 1
while (i <= lim):
	s = i * num
	print(i, "*", num, "=", s)
	i=i+1    
