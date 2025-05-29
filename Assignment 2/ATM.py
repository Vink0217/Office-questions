'''
11. ATM Machine Simulation
PIN-based login
View balance, withdraw, deposit, mini statement
Validate limits and handle errors
Concepts: Classes, exception handling, persistent user data in files
'''

from tkinter import *
from tkinter import messagebox
import json
import os
from datetime import datetime

Data_file = r"Assignment 2\InputOutput Files\UserData.json"

# Ensure file and correct encoding setup
if not os.path.exists(Data_file):
    user_data = {
        "1234": {"balance": 1000.0, "transactions": []}
    }
    with open(Data_file, "w", encoding="utf-8") as f:
        json.dump(user_data, f, ensure_ascii=False)
else:
    with open(Data_file, "r", encoding="utf-8") as f:
        user_data = json.load(f)

class ATM:
    def __init__(self, pin):
        if pin not in user_data:
            raise ValueError("Invalid PIN.")
        self.pin = pin
        self.data = user_data[pin]

    def get_balance(self):
        return self.data["balance"]

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        self.data["balance"] += amount
        self._add_transaction(f"Deposited ₹{amount:.2f}")
        self._save()

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.data["balance"]:
            raise ValueError("Insufficient balance.")
        self.data["balance"] -= amount
        self._add_transaction(f"Withdrew ₹{amount:.2f}")
        self._save()

    def get_mini_statement(self):
        return self.data["transactions"][-5:]

    def _add_transaction(self, desc):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data["transactions"].append(f"{time} - {desc}")

    def _save(self):
        user_data[self.pin] = self.data
        with open(Data_file, "w", encoding="utf-8") as f:
            json.dump(user_data, f, ensure_ascii=False)

class ATMApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("ATM Machine")
        self.geometry("400x500")
        self.atm = None
        self.entered_pin = ""
        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        Label(self, text="Enter PIN", font=("Arial", 16)).pack(pady=10)
        self.pin_var = StringVar()
        self.pin_entry = Entry(self, textvariable=self.pin_var, font=("Arial", 18), show="*", justify="center", width=10)
        self.pin_entry.pack(pady=10)

        frame = Frame(self)
        frame.pack()
        
        nums = [1,2,3,4,5,6,7,8,9]
        for i, num in enumerate(nums):
            Button(frame, text=str(num), width=5, height=2, command=lambda n=num: self.append_pin(n)).grid(row=i//3, column=i%3, padx=5, pady=5)
        Button(frame, text="0", width=5, height=2, command=lambda: self.append_pin(0)).grid(row=3, column=1)
        Button(frame, text="Clear", width=5, height=2, command=self.clear_pin).grid(row=3, column=0)
        Button(frame, text="Enter", width=5, height=2, command=self.validate_login).grid(row=3, column=2)

    def append_pin(self, number):
        self.entered_pin += str(number)
        self.pin_var.set("*" * len(self.entered_pin))

    def clear_pin(self):
        self.entered_pin = ""
        self.pin_var.set("")

    def validate_login(self):
        try:
            self.atm = ATM(self.entered_pin)
            self.entered_pin = ""
            self.main_menu()
        except ValueError:
            messagebox.showerror("Error", "Invalid PIN")
            self.clear_pin()

    def main_menu(self):
        self.clear_screen()
        Label(self, text="ATM Main Menu", font=("Arial", 16)).pack(pady=10)
        Button(self, text="View Balance", command=self.view_balance).pack(pady=5)
        Button(self, text="Deposit", command=self.deposit_screen).pack(pady=5)
        Button(self, text="Withdraw", command=self.withdraw_screen).pack(pady=5)
        Button(self, text="Mini Statement", command=self.show_statement).pack(pady=5)
        Button(self, text="Logout", command=self.login_screen).pack(pady=20)

    def view_balance(self):
        balance = self.atm.get_balance()
        messagebox.showinfo("Balance", f"Current Balance: ₹{balance:.2f}")

    def deposit_screen(self):
        self.transaction_screen("Deposit")

    def withdraw_screen(self):
        self.transaction_screen("Withdraw")

    def transaction_screen(self, action):
        self.clear_screen()
        Label(self, text=f"{action} Amount", font=("Arial", 14)).pack(pady=10)
        amount_entry = Entry(self, width=20)
        amount_entry.pack(pady=5)

        def process():
            try:
                amount = float(amount_entry.get())
                if action == "Deposit":
                    self.atm.deposit(amount)
                else:
                    self.atm.withdraw(amount)
                messagebox.showinfo("Success", f"{action} successful.")
                self.main_menu()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        Button(self, text=action, command=process).pack(pady=10)
        Button(self, text="Back", command=self.main_menu).pack(pady=5)

    def show_statement(self):
        transactions = self.atm.get_mini_statement()
        message = "\n".join(transactions) if transactions else "No transactions yet."
        messagebox.showinfo("Mini Statement", message)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = ATMApp()
    app.mainloop()
