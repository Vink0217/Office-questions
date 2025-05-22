'''
Q19) Expense Tracker 
Input daily Expenses and generate a weekly summary (store data in a file or dictionary). 
'''

Expenses = {}
file_path = "Output Files\Expenses.txt"

def Daily_Expenses():
    Day = str(input("Enter Day: ")).capitalize()
    Amount_Spent = int(input("Enter Spent Amount: ₹"))
    if Day not in Expenses:
        Expenses[Day] = []
    Expenses[Day].append(Amount_Spent)
    print(f"Added ₹{Amount_Spent} to {Day}")


def Weekly_summary():
    print("\nWeekly Expense Summary:")
    Total_Spent = 0
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        if day in Expenses:
            Daily_Expense = Expenses[day]
        else:
            Daily_Expense = []

        Daily_total = 0
        for amount in Daily_Expense:
            Daily_total += amount

        print(f"{day}: ₹{Daily_total}")
        Total_Spent += Daily_total
    print(f"\nTotal Spent: ₹{Total_Spent}")

def Store_File(file_path):
    with open(file_path, "w") as f:
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            daily_total = 0
            if day in Expenses:
                for amount in Expenses[day]:
                    daily_total += amount
            f.write(f"{day}:{daily_total}\n")
    print(f"Saved total per day to {file_path}")


Flag = True
while Flag:
    choice = int(input("\nEnter your Choice \n 1. Add Daily Expense \n 2. Show Weekly Summary \n 3. Exit \nChoose your option: "))

    if choice == 1:
        adding_stuff = True
        while adding_stuff:
            Daily_Expenses()
            ask = input("Do you want to add more? (Y/N): ").upper()
            if ask == "Y":
                continue
            elif ask == "N":
                Store_File(file_path)
                adding_stuff = False
            else:
                print("Wrong input")
    elif choice == 2:
        Weekly_summary()
    elif choice == 3:
        print("Exiting. Goodbye!")
        Flag = False
    else:
        print("Wrong option. Try again.")