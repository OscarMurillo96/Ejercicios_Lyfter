class BankAccount:
    def __init__(self, balance):
        self.balance = balance  #Account balance


    def add_amount(self, amount): #Function to add amount to the account
        self.balance += amount


    def withdraw_amount(self, amount): #Function to withdraw amount from the account
        self.balance -= amount


class SavingsAccount(BankAccount): #Inherits from BankAccount class
    def __init__(self, balance, min_balance):
        super().__init__(balance) #Inherits from the parent class
        self.min_balance = min_balance #Minimum balance


    def withdraw_amount(self, amount):
        if (self.balance - amount) < self.min_balance: #If the balance minus the amount is less than the minimum balance:
            raise ArithmeticError("Insufficient funds") #Raise an error
        else:
            super().withdraw_amount(amount) #Else, continue the operation


savings = SavingsAccount(1000, 200) #Account balance is 1000 and minimum balance is 200
savings.withdraw_amount(500) #Withdraw 500
print(savings.balance)

try: #Tries to withdraw 400
    savings.withdraw_amount(400)
except ArithmeticError as error:
    print(f"details: {error}") #Prints the error previously created in raise.