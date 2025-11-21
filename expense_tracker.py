import csv
from datetime import datetime

def add_expense(file_name):
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter Category (e.g. Food, Transportation, Entertainment):  ")
    description = input("Enter Description:  ")
    try:
        amount = float(input("Enter Amount:  "))
    except ValueError:
        print("Invalid amount.")
        return
    
    with open(file_name, mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

def view_expenses(file_name):
    try:
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            print("Date    | Category    | Description   | Amount")
            print('-'*50)
            for row in reader:
                print(f"{row[0]:<10} | {row[1]:<10} | {row[2]:<15} | £{float(row[3]):.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")
        
def main():
    file_name = "expenses.csv"
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense(file_name)
        elif choice == '2':
            view_expenses(file_name)
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid Choice.')
            
main()