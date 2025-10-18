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
                print(f"{txn["date"]} | {txn["time"]} | {txn["type"]} | {txn["ammount"]} TAKA | Balance : {txn["Balance"]} TAKA")

    def _add_transaction(self,txn_type,ammount):
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
    
class Bank:
    def __init__(self,bank_name,db_files="bank_data.txt"):
        self.bank_name = bank_name
        self.db_files = db_files
        self.account = {}
        self.last_account_number = 125101158000
        self.load_data()
        print(f"welcome to {self.bank_name} Bank!")

    def _load_data(self):
        if not os.path.exists(self.db_files):
            open (self.db_files,"w").close()
        with open(self.db_files, "r") as file:
                for line in file:
                    account = account.from_record(line)
                    if account:
                        self.accounts = [account.account_number] = account
                        self.last_account_number = max(self.last_account_number, int(account.account_number))
    def _save_data(self):
        with open(self.db_files, "w") as file:
            for account in self.accounts.values():
                file.write(account.to_record())

    def _generate_account_number(self):
        self.last_account_number += 1
        return str(self.last_account_number).zfill(13)
    
    def create_account(self,holder_name,initial_deposit = 0):
        account_number = self._generate_account_number
        new_account = account(account_number,holder_name,initial_deposit)
        self.accounts[account_number] = new_account
        self._save_data()
        print(f"account created for {self.holder_name}. Account number {self.account_number} ")
        return new_account

    def get_account(self,account_number):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found")
            return account
        
    def list_accounts(self):
        if not self.account:
            print("no accounts available.")
            return
        print("\n List all accounts")
        for acc_no, acc in self.accounts.items():
            print(f"A/C no {self.ac_no} ")

    def update_account(self,account):
        self.accounts[account.account_number] = account
        self._save_data()


class main():
    bank = Bank("NATIONAL BANK")

    while True:
        print("======================")
        print("1.Create new account")
        print("2.Deposit money")
        print("3.Withdraw money")
        print("4.Check balance")
        print("5.View transaction")
        print("6.List all accounts")
        print("Exit")
        print("======================")

        choise = input("enter your choise (1-7): ")

        if choise == 1:
            name = input("Enter account holder name: ")
            deposit = input("Enter initial deposit: ")
            bank.create_account(name,deposit)
        
        elif choise == "2":
                acc_no = input("Enter 13-digit account number: ")
                account . bank. get_account(acc_no)
                if account:
                    ammount = float(input("Enter deposit amount:"))
                    account.deposit(ammount)
                    bank. update_account (account)

        elif choise == "3":
                acc_no = input("Enter 13-digit account number: ")
                account = bank.get_account(acc_no)
                if account:
                    ammount - float(input("Enter withdrawal amount: "))
                    account.withdraw(ammount)
                    bank. update_account (account)

        elif choise == "4":
            acc_no . input("Enter 13-digit account number: ")
            account = bank.get_account(acc_no)
            if account:
                account.check_balance()

        elif choise == "5":
            acc_no - input("Enter 13-digit account number: ")
            account = bank.get_account(acc_no)
            if account:
              account.view_transactions()

        elif choise == "6":
            bank. list_accounts()

        elif choise == "7":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
        

        

        



        
        








        

    