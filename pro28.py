n=int(input("Enter the number of students:"))
d=int(input("Enter the number of days:"))
std_list=[]
for i in range(n):
    name=str(input("Enter the name of student:"))
    day=int(input("Enter the number of present days:"))
    per=(day/d)*100
    std_list.append((per,name))
    std_list.sort(reverse=True)
print(std_list)
