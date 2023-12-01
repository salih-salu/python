def add(num1,num2):
    sum=num1+num2
    return sum
def subtract(num1,num2):
    diff=num1-num2
    return diff
def multiply(num1,num2):
    mul=num1*num2
    return mul
def divide(num1,num2):
    div=num1/num2
    return div
def power(num1,num2):
    p=num1**num2
    return p
def calculator(num1,num2,oper):
    if oper == 1:
        print(add(num1,num2))    
    elif oper == 2:
        print(subtract(num1,num2))
    elif oper == 3:
        print(multiply(num1,num2))
    elif oper == 4:
        print(divide(num1,num2))
    elif oper == 5:
        print(power(num1,num2)) 
    else:
        print("Invalid choice...!!!")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print(" 1:Addition \n 2:Subtraction \n 3:Multiplication \n 4:Division \n 5:power")
oper=int(input("enter the operator:"))
calculator(num1,num2,oper)

    
