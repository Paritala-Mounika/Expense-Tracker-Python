from tkinter import *

expenses = []

def add_expense():
    name = entry_name.get()
    amount = entry_amount.get()

    if name != "" and amount != "":
        expenses.append((name, float(amount)))
        listbox.insert(END, f"{name} - ₹{amount}")

        entry_name.delete(0, END)
        entry_amount.delete(0, END)

def calculate_total():
    total = 0
    for expense in expenses:
        total += expense[1]

    total_label.config(text=f"Total Expense: ₹{total}")

# Main Window
root = Tk()
root.title("Expense Tracker")
root.geometry("550x550")

# Heading
Label(root, text="Expense Tracker",
      font=("Arial", 16, "bold")).pack(pady=10)

# Expense Name
Label(root, text="Expense Name").pack()
entry_name = Entry(root, width=30)
entry_name.pack(pady=5)

# Amount
Label(root, text="Amount").pack()
entry_amount = Entry(root, width=30)
entry_amount.pack(pady=5)

# Add Button
Button(root, text="Add Expense",
       command=add_expense).pack(pady=10)

# Listbox
listbox = Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Total Button
Button(root, text="Calculate Total",
       command=calculate_total).pack(pady=10)

# Total Label
total_label = Label(root,
                    text="Total Expense: ₹0",
                    font=("Arial", 12, "bold"))
total_label.pack(pady=10)

root.mainloop()
