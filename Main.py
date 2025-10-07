import os
from datetime import datetime

class account:
    def __init__(self,account_number,holder_name,balance = 0):
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance = balance
        self.transaction = []

    def deposit(self,ammount):
        if ammount <= 0:
            print("Deposit ammount must be greater than 0")
            return
        self.balance += ammount
        self.__add_transaction("deposit",ammount)
        print(f"Diposited {ammount} taka successfully. current balance {self.balance}.")

    def withdraw(self,ammount):
        if ammount <= 0:
            print("Withdrawn ammount must be greater than zero")
            return
        if ammount > self.balance:
            print("Insufficient fund.")
            return
        self.balance -= ammount
        self.__add_transaction("withdraw",-ammount)
        print(f"withdrawed {ammount} taka successfully. current balance {self.balance}.")

    def check_balance(self):
        print(f"Ammount balance for {self.holder_name} : {self.balance}")

    