# Create a Python class called BankAccount which represents a bank account, having as attributes: 
# Create a constructor with parameters: accountNumber (numeric type), first_name, last_name (name of the account owner as string type), balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create a display() method to display account details.
# create a function main  the complete code for the  BankAccount class.
# Initialization of a new account
# Please enter new account number: 123
# Please enter client first name: el
# Please enter client last name: zakai
# please enter new account balance: 200
# Account created for el zakai, with the number: 123 and a balance of 200 $USD
# To quit enter q, to create another account enter a to deposit enter d and to withdraw enter w:
# # chose d w (if over amount message if under deduct form balance 
# initializing deposit of 234 usd
# the balance before deposit for account 123 is 200 $US



import sys

accounts = {}
class BankAccount:

    # create the constuctor with parameters: accountNumber, name and balance
    def __init__(self, accountnumber, firstname, lastname, balance=0):
        self.lastname = lastname
        self.accountNumber = accountnumber
        self.firstname = firstname
        self.balance = balance
        accounts[self.accountNumber] = [self.firstname,self.lastname,self.balance]
        print(f"Account created for {firstname} {lastname}, with the number: {accountnumber} and a balance of {balance} $USD")
    # create Deposit() method
    def Deposit(self, d):
        print(f"initializing deposit of {d} usd")
        print(f"the balance before deposit for account {self.accountNumber} is {self.balance} $USD")
        self.balance = self.balance + d
        print(f"the balance after deposit for account {self.accountNumber} is {self.balance} $USD")
    # create Withdrawal method

    def Withdrawal(self, w):
        if self.balance < w:
            print("impossible operation! Insufficient balance !")
        else:
            print(f"initializing withdrawal of {w} $USD")
            print(f"the balance before withdrawal for account {self.accountNumber} is {self.balance} $USD")
            self.balance = self.balance - w
            print(f"the balance after withdrawal for account {self.accountNumber} is {self.balance} $USD")
    # create bankFees() method
    def bankFees(self):
        print(f"the balance before fees for account {self.accountNumber} is {self.balance}")
        self.balance = (95 / 100) * self.balance
        print(f"the balance after fees for account {self.accountNumber} is {self.balance}")
    # create display() method
    def display(self):
        print(f"Account Number : ", self.accountNumber)
        print(f"Account Name : {self.firstname}{self.lastname}")
        print(f"Account Balance :  {self.balance}  $USD")


def main_run():
    flag = True
    while flag:
        print("Initialization of a new account")
        accountnumber = int(input("Please enter new account number: "))
        firstname = input("Please enter client first name: ")
        lastname = input("Please enter client last name: ")
        balance = int(input("please enter new account balance: "))
        newAccount = BankAccount(accountnumber, firstname, lastname, balance)
        choice = input("To quit enter q, to create another account enter a to deposit enter d and to withdraw enter w: ")
        if choice.lower() == 'q':
            print(f"accounts created this session: ")
            print(accounts)
            sys.stdout = open('report1.txt', 'w')
            print(accounts)
            print("again")
            flag = False
        elif choice == 'a':
            continue
        elif choice == 'd':
            amount = int(input("Please enter amount to deposit: "))
            newAccount.Deposit(amount)
        elif choice == "w":
            amount = int(input("Please enter amount to withdraw: "))
            newAccount.Withdrawal(amount)




main_run()






