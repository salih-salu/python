y = { }
n=int(input("Enter the number of students:"))
for i in range(n):
    print("Enter the details of student",i+1)
    name=input("Enter name of student:")
    age=input("Enter the Age:")
    y[name]=age
print("------------------------------------------------")
print("You inserted dictionary is:")
print(y)
print("------------------------------------------------")
l=[]
l=list(y.items())
l.sort()
print("LIST")
print("Sorted items in Ascending order is:",l)
aa=dict(l)
print("DICTIONARY")
print(aa)
l.sort(reverse = True)
print("LIST")
print("Sorted items in Discending order is:",l)
dd=dict(l)
print("DICTIONARY")
print(dd)

