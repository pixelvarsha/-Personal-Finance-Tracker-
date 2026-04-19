from user import User
from manager import FinanceManager
from transaction import Transaction

def main():
    name = input("Enter your name: ")
    budget = float(input("Set your monthly budget: "))

    user = User(name, budget)
    manager = FinanceManager()
    manager.load_from_csv()

    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Show Chart")
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                amt = float(input("Enter income amount: "))
                cat = input("Enter category: ")
                date = input("Enter date: ")
                manager.add_transaction(Transaction(amt, cat, date, "income"))

            elif choice == "2":
                amt = float(input("Enter expense amount: "))
                cat = input("Enter category: ")
                date = input("Enter date: ")
                manager.add_transaction(Transaction(amt, cat, date, "expense"))

                if manager.total_expenses() > user.get_budget():
                    print("⚠️ Budget exceeded!")

            elif choice == "3":
                print("Total Income:", manager.total_income())
                print("Total Expenses:", manager.total_expenses())
                print("Savings:", manager.savings())

            elif choice == "4":
                manager.show_chart()

            elif choice == "5":
                manager.save_to_csv()
                print("Data saved. Exiting...")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("❌ Invalid input! Please enter correct values.")

if __name__ == "__main__":
    main()
