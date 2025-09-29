#!/usr/bin/python3
class BankAccount:
    def __init__(self, initial_balance=0):
        """Initializes the account with a given balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Adds a specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraws a specified amount if funds are sufficient."""
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Prints the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
