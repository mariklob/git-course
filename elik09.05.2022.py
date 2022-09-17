# insert in console
# Please enter emp id: 5555
# Please enter first name : Mark
# Please enter last name : Davidi
# please enter salary: 7000
# creating and display commands:
# [5:23 PM] employee id: 5555
# employee full name: Mark Davidi
# employee salary: 7000
# employee annual salary is: Mark Davidi 84000
# Next command:
# Salary before raise is: 7000
# Salary after raise is: 7500
# New annual salary is Mark Davidi 90000
# Next command:
# Salary before raise is: 7500
# Salary after raise is: 8000
# New annual salary is Mark Davidi 96000



class Employee:

    # create the constuctor with parameters: accountNumber, name and balance
    def __init__(self,id, firstname, lastname, salary=0):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.salary = salary
        print(f"Account created for {firstname} {lastname}, with the number: {salary} and a balance of {balance} $USD")
    # create Deposit() method
    def (self, d):
        print(f"initializing deposit of {d} usd")
        print(f"the balance before deposit for account {self.accountNumber} is {self.balance} $USD")
        self.balance = self.balance + d
        print(f"the balance after deposit for account {self.accountNumber} is {self.balance} $USD")
    # create Withdrawal method
