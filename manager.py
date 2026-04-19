import csv
from transaction import Transaction
import matplotlib.pyplot as plt

class FinanceManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def save_to_csv(self, filename="data.csv"):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Amount", "Category", "Date", "Type"])
                for t in self.transactions:
                    writer.writerow(t.to_list())
        except Exception as e:
            print("Error saving file:", e)

    def load_from_csv(self, filename="data.csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    amount, category, date, t_type = row
                    self.transactions.append(
                        Transaction(float(amount), category, date, t_type)
                    )
        except FileNotFoundError:
            print("No previous data found.")

    def total_expenses(self):
        return sum(t.amount for t in self.transactions if t.type == "expense")

    def total_income(self):
        return sum(t.amount for t in self.transactions if t.type == "income")

    def savings(self):
        return self.total_income() - self.total_expenses()

    def category_analysis(self):
        data = {}
        for t in self.transactions:
            if t.type == "expense":
                data[t.category] = data.get(t.category, 0) + t.amount
        return data

    def show_chart(self):
        data = self.category_analysis()
        categories = list(data.keys())
        amounts = list(data.values())

        plt.bar(categories, amounts)
        plt.title("Expense Analysis")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()
