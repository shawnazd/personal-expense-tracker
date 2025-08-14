
# 💸 Personal Expense Tracker

Keep track of your **daily expenses** effortlessly with this Python-based **Personal Expense Tracker**. 📝  
All your data is automatically saved in a JSON file so you never lose your records! 💾

---

## ✨ Features

- 🆕 **Add Expense** – Record expenses with date, category, amount, and description.  
- 📋 **View All Expenses** – Display all saved expenses in a neat table.  
- 📊 **Summary by Category** – See your total spending grouped by category.  
- 🔍 **Filter/Search Expenses** – Quickly find expenses by keyword.  
- 💾 **Automatic Data Storage** – Data is saved in `expenses.json`, created automatically on first run.

---

## 🛠 Installation

1. Clone this repository:

```bash
git clone https://github.com/shawnazd/personal-expense-tracker.git
````

2. Navigate to the project folder:

```bash
cd personal-expense-tracker
```

3. Make sure Python 3 is installed:

```bash
python --version
```

---

## ▶️ How to Run

Run the main Python program:

```bash
python expense_tracker.py
```

> ℹ️ **Note:** On first run, `expenses.json` will be automatically created in the project folder.

---

## 📝 Usage

After running, you'll see this menu:

```
=== Personal Expense Tracker ===
1. Add Expense
2. View All Expenses
3. Summary by Category
4. Filter/Search Expenses
5. Exit
Choose an option:
```

### Options Explained:

1. 🆕 **Add Expense** – Enter date (leave blank for today), category, amount, and description.
2. 📋 **View All Expenses** – Displays all saved expenses in a formatted table.
3. 📊 **Summary by Category** – Shows total spending per category.
4. 🔍 **Filter/Search Expenses** – Search expenses by keyword in category or description.
5. ❌ **Exit** – Exit the program safely.

---

## 💾 Example JSON Structure (`expenses.json`)

```json
[
  {
    "date": "2025-08-14",
    "category": "Food",
    "amount": 2500.0,
    "description": "Lunch 🍔"
  },
  {
    "date": "2025-08-14",
    "category": "Transport",
    "amount": 1500.0,
    "description": "Bus fare 🚌"
  }
]
```

> The JSON file is updated automatically whenever you add a new expense. 🚀

---

## 📖 License

This project is **open-source** and free to use. ❤️

```

