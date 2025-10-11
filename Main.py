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
    
    def view_transaction(self):
        print(f"\n Transaction history for {self.hoder_name}")
        if not self.transaction:
            print("No transaction history available for this account.")
            for txn in self.transaction:
                print(f"{txn["date"]} | {txn["time"]} | {txn["type"]} | {txn["ammount"]} TAKA | Balance : {txn["balance"]} TAKA")

    def __add_transaction(self,txn_type,ammount):
        txn = {
            "date" : datetime.now().strftime("%Y-%M-%d H%:%M:%S"),
            "type" : txn_type,
            "ammount" : ammount,
            "Balance" : self.balance
        }

        self.transaction.append(txn)

    def to_record(self):
        txn_data = ";".join(
            [f"{t['date']} , {t["type"]} , {t["ammount"]} , {t["Balance"]}" for t in self.transaction]
        )
        return f"{self.account_number} | {self.holder_name} | {self.balance} | {txn_data} "
    
    @staticmethod
    def from_record(line):
        parts = line.strip().split("|")
        if len[parts] > 4:
            return None
    
        account_number = parts[0]
        holder_name = parts[1]
        balance = float(parts[2])
        account = account(account_number,holder_name,balance)
        txn_data = parts[3]

        if txn_data:
           for txn_str in txn_data.split(";"):
               t_parts = txn_str.split(",")
               if len(t_parts) == 4:
                   account.transaction.appenend({
                       "date" : t_parts[0],
                       "type" : t_parts[1],
                       "ammount" : float(t_parts[2])
                       "Balance" : float(t_parts[3])
                   })
        return account


        

    