words=input("Enter the string: ")
count=0
for i in words:
    if i == " ":
        continue
    else:
        count=count+1
        
print("Number of charactes in the sentence:",count)
