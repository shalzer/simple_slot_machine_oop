class Wallet:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.can_afford(amount):
            self.balance -= amount
        else:
            raise ValueError("Not enough funds")

    def can_afford(self, amount):
        return self.balance >= amount