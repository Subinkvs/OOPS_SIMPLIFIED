# write a program to simulate a bank account using OOP ?


class BankAccount:
    def __init__(self, initial_amount):
        self.balance = initial_amount   

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}, New Balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount}, New Balance: {self.balance}"
        else:
            return "Insufficient funds"

    def check_balance(self):
        return f"Current Balance: {self.balance}"

# Using OOP
account1 = BankAccount(1000)
print(account1.deposit(500))
print(account1.withdraw(300))
print(account1.check_balance())
