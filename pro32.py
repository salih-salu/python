class account:
	def __init__(self):
		self.balance=0
		
	def deposit(self):
		amount=int(input("Enter the amount to be deposit : "))
		self.balance+=amount
	def withdraw(self):
		amount=int(input("Enter the amount to be withdraw : "))
		if amount > self.balance :
			print("invalid bank account balance!!! \n please check account balance!!!")
		else:
			self.balance -= amount
			print(amount,"is withdraw")
			
	def display(self):
		print("BANK ACCOUNT BALANCE IS : ",self.balance)
			
	
myaccount=account()
while(choice):
	print("\na:DEPOSIT \nb:WITHDRAW \nc:DISPALY \nd:EXIT \n")
	choice=str(input("Enter the choice:"))
	match choice:
		case "a":
			myaccount.deposit()
			break
		case "b":
			myaccount.withdraw()
			break
		case "c":
			myaccount.display()	
			break
		case _:
			print("invalid choice!!")
			break
			
		



