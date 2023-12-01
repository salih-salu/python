n=int(input("Enter the number of elements:"))
ch=[]
max=0
for i in range(n):
    ch.append(input("Enter the value:"))
    if(len(ch[i])>max):
        max=len(ch[i])
        chs=ch[i]    
print("Longest string is ",chs,"with length ",max)
