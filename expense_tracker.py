# Expense Tracker in Python

def show_menu():
    print("\n==========================================")
    print("           EXPENSE TRACKER                ")
    print("==========================================")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Show total expenses")
    print("4. Exit")

def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount ($): "))
        category = input("Enter category (e.g., Food, Transport, Bills): ").strip()
        description = input("Enter brief description: ").strip()
        
        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount! Please enter a valid number.")

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n------------------------------------------")
    print("             ALL EXPENSES                 ")
    print("------------------------------------------")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. Category: {exp['category']} | Amount: ${exp['amount']:.2f} | Note: {exp['description']}")
    print("------------------------------------------")

def total_expenses(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")
            

def main():
    expenses = []
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total_expenses(expenses)
        elif choice == '4':
            print("Thank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")

if __name__ == "__main__":
    main()
