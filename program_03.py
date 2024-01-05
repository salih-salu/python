print("Area of a triangle")
a = int(input("Enter side A = "))
b = int(input("Enter side B = "))
c = int(input("Enter side C = "))
s = (a + b + c) / 2 
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print("Area = ", area)
