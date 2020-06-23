# Error handling
import random
print('\t\t\t\t|_BANK_|')
print('''\n
	|_open 24*7_|	   |_HDFC BANK_|
	''')


class BankAccount:
	def __init__(self,name, aadhar,pan_card, deposit=10000):
		self.name = name
		self.aadhar = aadhar
		self.pan_card = pan_card
		self.deposit = deposit
		self.account_no = random.randint(10000000,99999999)
		self.pin = random.randint(1000,9999)
		self.limit = random.randint(4,7)
    

	def PassBook(self):
		print(f'''
		      your account created successfully..
			  Detail:
			         name : {self.name}
					 account no : {self.account_no}
					 aadhar: {self.aadhar}
					 pan no : {self.pan_card}
					 pin : {self.pin}
		''')

print('''
	| Choose Our Service |\n
			1. Create Bank Account
			2. deposit Money
			3. Chack PassBook
			4. Withdraw money
	5. exit
''')
client1 = BankAccount('deepak','1234','3456')
client2 =
user_input = int(input('..'))
