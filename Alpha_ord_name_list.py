n=int(input("Enter the number of names: "))
names=[]
for i in range(n):
    name=input("Enter the name:")
    names.append(name)
    names.sort()
for name in names:
    print(name)
