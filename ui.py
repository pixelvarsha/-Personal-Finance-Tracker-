import tkinter as tk
from tkinter import messagebox
from manager import FinanceManager
from transaction import Transaction

# Initialize
manager = FinanceManager()
manager.load_from_csv()

# Main Window
root = tk.Tk()
root.title("Finance Tracker - Live Dashboard")
root.geometry("650x750")
root.configure(bg="#0f172a")

# ---------- SHADOW CARD FUNCTION ----------
def create_card(parent, title):
    shadow = tk.Frame(parent, bg="#020617")
    shadow.pack(pady=10, padx=20, fill="x")

    card = tk.Frame(shadow, bg="#1e293b")
    card.pack(padx=4, pady=4, fill="x")

    tk.Label(card, text=title, bg="#1e293b", fg="white",
             font=("Segoe UI", 14, "bold")).pack(anchor="w", padx=15, pady=10)

    inner = tk.Frame(card, bg="#1e293b")
    inner.pack(padx=15, pady=10)

    return inner

# ---------- DASHBOARD UPDATE ----------
def update_dashboard():
    income = manager.total_income()
    expense = manager.total_expenses()
    savings = manager.savings()

    income_label.config(text=f"₹ {income}")
    expense_label.config(text=f"₹ {expense}")
    savings_label.config(text=f"₹ {savings}")

    root.after(1000, update_dashboard)  # auto refresh every 1 sec

# ---------- DASHBOARD CARD ----------
dash_card = create_card(root, "📊 Live Dashboard")

income_label = tk.Label(dash_card, text="₹ 0", bg="#1e293b", fg="#22c55e", font=("Segoe UI", 16, "bold"))
income_label.grid(row=0, column=0, padx=20)

tk.Label(dash_card, text="Income", bg="#1e293b", fg="white").grid(row=1, column=0)

expense_label = tk.Label(dash_card, text="₹ 0", bg="#1e293b", fg="#ef4444", font=("Segoe UI", 16, "bold"))
expense_label.grid(row=0, column=1, padx=20)

tk.Label(dash_card, text="Expense", bg="#1e293b", fg="white").grid(row=1, column=1)

savings_label = tk.Label(dash_card, text="₹ 0", bg="#1e293b", fg="#38bdf8", font=("Segoe UI", 16, "bold"))
savings_label.grid(row=0, column=2, padx=20)

tk.Label(dash_card, text="Savings", bg="#1e293b", fg="white").grid(row=1, column=2)

# ---------- INPUT CARD ----------
input_card = create_card(root, "💳 Add Transaction")

amount_entry = tk.Entry(input_card, bg="#334155", fg="white", insertbackground="white", width=25)
amount_entry.grid(row=0, column=0, padx=10, pady=10)
amount_entry.insert(0, "Amount")

category_entry = tk.Entry(input_card, bg="#334155", fg="white", insertbackground="white", width=25)
category_entry.grid(row=0, column=1, padx=10, pady=10)
category_entry.insert(0, "Category")

date_entry = tk.Entry(input_card, bg="#334155", fg="white", insertbackground="white", width=25)
date_entry.grid(row=1, column=0, padx=10, pady=10)
date_entry.insert(0, "Date")

# ---------- FUNCTIONS ----------
def add_income():
    try:
        amt = float(amount_entry.get())
        manager.add_transaction(Transaction(amt, category_entry.get(), date_entry.get(), "income"))
        messagebox.showinfo("Success", "Income Added")
    except:
        messagebox.showerror("Error", "Invalid Input")


def add_expense():
    try:
        amt = float(amount_entry.get())
        manager.add_transaction(Transaction(amt, category_entry.get(), date_entry.get(), "expense"))
        messagebox.showinfo("Success", "Expense Added")
    except:
        messagebox.showerror("Error", "Invalid Input")

# ---------- BUTTON CARD ----------
button_card = create_card(root, "⚡ Actions")

tk.Button(button_card, text="Add Income", command=add_income,
          bg="#22c55e", fg="black", width=15).grid(row=0, column=0, padx=10, pady=10)

tk.Button(button_card, text="Add Expense", command=add_expense,
          bg="#ef4444", fg="black", width=15).grid(row=0, column=1, padx=10, pady=10)

# ---------- ANALYTICS CARD ----------
def show_chart():
    manager.show_chart()


def save_data():
    manager.save_to_csv()
    messagebox.showinfo("Saved", "Data Saved")

extra_card = create_card(root, "📈 Analytics")

tk.Button(extra_card, text="Show Chart", command=show_chart,
          bg="#a855f7", fg="white", width=15).grid(row=0, column=0, padx=10, pady=10)

tk.Button(extra_card, text="Save Data", command=save_data,
          bg="#facc15", fg="black", width=15).grid(row=0, column=1, padx=10, pady=10)

# Footer
footer = tk.Label(root, text="Made with ❤ by Aakanksha", bg="#0f172a", fg="#64748b")
footer.pack(pady=10)

# Start live updates
update_dashboard()

# Run App
root.mainloop()
