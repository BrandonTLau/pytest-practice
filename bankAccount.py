'''
variables: 


functions: 

Constructor
    Creates an account with a starting balance
    Default balance is 0 if none provided
    Raises ValueError if starting balance is negative

deposit(amount)
    Adds amount to balance
    Returns the new balance
    Raises ValueError if amount is zero or negative

withdraw(amount)
    Subtracts amount from balance
    Returns the new balance
    Raises ValueError if amount is zero or negative
    Raises ValueError if amount exceeds current balance (no overdraft)

get_balance()
    Returns the current balance

transfer(amount, target_account)
    Withdraws from self, deposits into target_account
    Raises ValueError if amount exceeds current balance
    Both accounts should update correctly

transaction_history
    A list that records every deposit and withdrawal as a string
    Format: "Deposited: 100", "Withdrew: 50"
    Transfers count as both a withdrawal on one account and a deposit on the other
'''

class BankAccount:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Value Error: Balance is less than 0.")
        self.balance = balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Value Error: Deposit amount must be positive.")
        self.balance = self.balance + amount
        self.transaction_history.append(f"Deposited: {amount}")
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Value Error: Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance = self.balance - amount
        self.transaction_history.append(f"Withdrew: {amount}")
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, target_account):
        self.withdraw(amount)
        target_account.deposit(amount)




    