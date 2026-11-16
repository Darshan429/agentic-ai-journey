class BankAccount:
    def __init__(self,name,balance=0):
        self.name = name
        self._balance = balance
        #removed self.error

    def __str__(self):
        return f"Bank Account Details: owner = {self.name}, balance = {self._balance}"

    def check_balance(self):
        print(f"Your current Balance is: {self._balance}")
        return self._balance

    def deposit(self,amount):
        if(amount <= 0):
            print("Amount cannot be negative")
            return self._balance
        self._balance += amount
        print(f"Current Balance is: {self._balance}")
        return self._balance

    def withdraw(self,amount):
        if(amount <= 0):
            print("Withdrawl amount must be greater than zero")
            return False
        if(self._balance < amount):
            print("Insufficient Balance!")
            return False
        print("Request processing...")
        self._balance -= amount
        print("Amount withdrawn successfully!")
        print(f"Current Balance is: {self._balance}")
        return True

class SavingsAccount(BankAccount):
    # Here rate is percentage,It credits that rate% of cuurent balance to user account
    def add_interest(self,rate=5):
        interest = (rate/100) * self._balance
        self._balance += interest
        print(f"{rate}% interest is credited to your account successfuly!\n Your current balance: {self._balance}")
        return self._balance


user1 = BankAccount('Dave',100000)
print(user1)
user1.deposit(10000)
user1.check_balance()
user1.withdraw(10000)
user1.withdraw(-123)
user1.withdraw(10000000)

print(user1._balance = 5)

user2 = SavingsAccount('James',100000)
user2.add_interest()

user1._balance = 5


demo_user = BankAccount('William',1000)
demo_saving_acc = SavingsAccount('Jake',1000)


assert demo_user.deposit(500) == 1500, "After deposit current balance should increased to added amount"
assert demo_user.withdraw(0) == False, "Withdrawl amount cannot be zero"
assert demo_saving_acc.add_interest(5) == 1000+(5/100) * 1000, "Only specified rate amount should be credited"


1050.00 == 1050