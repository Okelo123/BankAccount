import random
from datetime import datetime

class BankAccount:
    def __init__(self, id_number, customer_name, balance=0.0):
        self.id_number = id_number  # User's ID number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = datetime.now().strftime('%Y-%m-%d')
        self.account_number = self.generate_account_number()
        self.transactions = []  # List to store transaction history

    def generate_account_number(self):
        return random.randint(1000000000, 9999999999)

    def deposit(self, amount):
        self.balance += amount
        transaction_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transactions.append({
            'type': 'Deposit',
            'amount': amount,
            'balance': self.balance,
            'time': transaction_time
        })
        return amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            transaction_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.transactions.append({
                'type': 'Withdraw',
                'amount': amount,
                'balance': self.balance,
                'time': transaction_time
            })
            return amount

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Account Opening: {self.date_of_opening}")
        
    def mini_statement(self):
        if not self.transactions:
            print("No transactions found.")
        else:
            print("\nMini Statement:")
            for transaction in self.transactions:
                print(f"{transaction['time']} - {transaction['type']}: {transaction['amount']} | Balance: {transaction['balance']}")
        

class Bank:
    def __init__(self):
        self.accounts = {}

    def register_account(self, customer_name, id_number):
        if id_number in self.accounts:
            print("ID number already exists.")
            return
        new_account = BankAccount(id_number, customer_name)
        self.accounts[id_number] = new_account
        print(f"Account successfully created for {customer_name}. Your account number is {new_account.account_number}.")

    def perform_operations(self, id_number):
        if id_number not in self.accounts:
            print("Account not found.")
            return

        account = self.accounts[id_number]

        while True:
            print("\nSelect operation:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. View Customer Details")
            print("5. View Mini Statement")

            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                print(f"Amount Deposited: {account.deposit(amount)}")
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                print(f"Amount Withdrawn: {account.withdraw(amount)}")
                account.check_balance()
            elif choice == "3":
                account.check_balance()
            elif choice == "4":
                account.customer_details()
            elif choice == "5":
                account.mini_statement()
            else:
                print("Invalid choice, please try again.")

bank = Bank()
customer_name = input("Enter your name: ")
id_number = input("Enter your ID number: ")

bank.register_account(customer_name, id_number)
bank.perform_operations(id_number)
