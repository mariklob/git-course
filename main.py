
class Account:

    def __init__ (self,id,name,balance):
        self.id = id
        self.name = name
        self.balance = balance


#function returne balance after account crediter
    def credit(self,amount):
        self.balance += amount
        return self.balance


acc1 = Account(11,"Elik",0)

print(acc1.id)
