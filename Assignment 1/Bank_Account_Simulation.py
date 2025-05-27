'''
Q15) Bank Account Simulation 
Create a BankAccount class with deposit, withdraw, and balance inquiry methods. 
'''
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money to withdraw.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

accounts = {
    "Vinayak": BankAccount("Vinayak", 100),
    "Ahmed": BankAccount("Ahmed", 200)
}


while True:
    name = input("\nEnter your name (or type 'exit' to quit): ")
    if name.lower() == 'exit':
        break

    if name in accounts:
        account = accounts[name]
        choice = int(input("Enter your choice:\n 1. Check Balance\n 2. Deposit Cash\n 3. Withdraw Cash\nChoose option: "))
        if choice == 1:
            account.check_balance()
        elif choice == 2:
            deposit_money = int(input("Enter amount to deposit: ₹"))
            account.deposit(deposit_money)
        elif choice == 3:
            withdraw_money = int(input("Enter amount to withdraw: ₹"))
            account.withdraw(withdraw_money)
        else:
            print("Invalid choice.")
    else:
        print("Account not found.")

