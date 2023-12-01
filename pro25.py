student = { }
n=int(input("Enter the number of students:"))
for i in range(n):
    print("Enter the details of student",i+1)
    name=input("Enter name of student:")
    age=input("Enter the Age:")
    grade=input("Enter the Gade:")
    student[name]=age,grade
print(student)
