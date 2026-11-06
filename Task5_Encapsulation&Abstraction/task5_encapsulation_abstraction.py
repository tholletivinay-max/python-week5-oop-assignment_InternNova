
# TASK 5: ENCAPSULATION AND ABSTRACTION

from abc import ABC, abstractmethod

# Abstract class
class BankAccount(ABC):

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount!")

    # Abstract method
    @abstractmethod
    def account_details(self):
        pass


# Child class
class SavingsAccount(BankAccount):

    # Implementing abstract method
    def account_details(self):
        print("\nACCOUNT DETAILS")
        print("----------------------------")
        print("Account Holder:", self.account_holder)
        print("Account Type: Savings Account")
        print("Account Balance: Rs.", self.get_balance())
        print("----------------------------")

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            print("Amount deposited: Rs.", amount)
        else:
            print("Invalid deposit amount!")

    # Withdraw method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print("Amount withdrawn: Rs.", amount)
        else:
            print("Insufficient balance or invalid amount!")


# Creating an object
account = SavingsAccount("Vinay", 10000)

print("BANK ACCOUNT MANAGEMENT SYSTEM")
print("================================")

# Display account details
account.account_details()

# Deposit money
print("\nDEPOSIT OPERATION")
account.deposit(2000)

# Withdraw money
print("\nWITHDRAWAL OPERATION")
account.withdraw(1500)

# Display updated balance
print("\nUPDATED ACCOUNT DETAILS")
account.account_details()
