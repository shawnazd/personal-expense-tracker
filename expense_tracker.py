import json
import os
from datetime import datetime
from collections import defaultdict

FILENAME = 'expenses.json'

# Load expenses from JSON
def load_expenses():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Save expenses to JSON
def save_expenses(expenses):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(expenses, f, indent=4)

# Add a new expense
def add_expense():
    while True:
        date = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')
            break
        try:
            datetime.strptime(date, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")

    category = input("Enter category (Food, Transport, Shopping, etc.): ").strip()

    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    description = input("Enter description: ").strip()

    expenses = load_expenses()
    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })
    save_expenses(expenses)
    print("✅ Expense added successfully!")

# Helper function to print tables
def print_table(rows, headers):
    if not rows:
        print("No data to display.")
        return
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, value in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(value)))

    header_row = " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
    print(header_row)
    print("-" * (sum(col_widths) + 3 * (len(headers)-1)))

    for row in rows:
        print(" | ".join(f"{str(row[i]):<{col_widths[i]}}" for i in range(len(headers))))

# View all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    headers = ["Date", "Category", "Amount", "Description"]
    rows = [[e["date"], e["category"], e["amount"], e["description"]] for e in expenses]
    print("\nAll Expenses:")
    print_table(rows, headers)

# Summary by category
def summary_by_category():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to summarize.")
        return
    totals = defaultdict(float)
    for e in expenses:
        totals[e["category"]] += e["amount"]

    headers = ["Category", "Total Amount"]
    rows = [[cat, total] for cat, total in totals.items()]
    print("\nExpense Summary by Category:")
    print_table(rows, headers)

# Filter/Search expenses
def filter_expenses():
    keyword = input("Enter keyword to search in description or category: ").strip().lower()
    expenses = load_expenses()
    filtered = [e for e in expenses if keyword in e["category"].lower() or keyword in e["description"].lower()]
    if not filtered:
        print(f"No expenses matching '{keyword}' found.")
        return
    headers = ["Date", "Category", "Amount", "Description"]
    rows = [[e["date"], e["category"], e["amount"], e["description"]] for e in filtered]
    print(f"\nFiltered Expenses (keyword: '{keyword}'):")
    print_table(rows, headers)

# Main menu
def menu():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Summary by Category")
        print("4. Filter/Search Expenses")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summary_by_category()
        elif choice == '4':
            filter_expenses()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
