import os
from datetime import datetime
from colorama import Fore, Style
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# File to store expenses
EXPENSES_FILE = "expenses.txt"
PDF_REPORT_FILE = "expense_summary.pdf"

# Ensure the file exists
def ensure_file():
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'w') as file:
            file.write("Category,Amount,Date\n")

# Add an expense to the file
def add_expense():
    print(Fore.BLUE + "Add an Expense" + Style.RESET_ALL)
    category = input(Fore.YELLOW + "Enter category (e.g., Food, Travel): " + Style.RESET_ALL).strip()
    amount = input(Fore.YELLOW + "Enter amount: " + Style.RESET_ALL).strip()
    date = input(Fore.YELLOW + "Enter date (YYYY-MM-DD): " + Style.RESET_ALL).strip()

    # Validate date format
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(Fore.RED + "Invalid date format. Please use YYYY-MM-DD." + Style.RESET_ALL)
        return

    # Append the expense to the file
    with open(EXPENSES_FILE, 'a') as file:
        file.write(f"{category},{amount},{date}\n")
    print(Fore.GREEN + "Expense added successfully!" + Style.RESET_ALL)

# View expenses by category
def view_expenses():
    print(Fore.BLUE + "\nExpenses by Category:" + Style.RESET_ALL)
    expenses = {}

    # Read all expenses
    with open(EXPENSES_FILE, 'r') as file:
        next(file)  # Skip header
        for line in file:
            category, amount, date = line.strip().split(',')
            if category not in expenses:
                expenses[category] = []
            expenses[category].append((amount, date))

    # Display expenses by category
    for category, entries in expenses.items():
        print(Fore.YELLOW + f"\n{category}:" + Style.RESET_ALL)
        if not entries:
            print(Fore.RED + "No expenses recorded." + Style.RESET_ALL)
        else:
            for amount, date in entries:
                print(f"- Amount: {amount} - Date: {date}")

# View monthly summary
def monthly_summary():
    print(Fore.BLUE + "\nMonthly Summary" + Style.RESET_ALL)
    month_year = input(Fore.YELLOW + "Enter month and year (MM-YYYY): " + Style.RESET_ALL).strip()
    try:
        datetime.strptime(month_year, "%m-%Y")  # Validate input
    except ValueError:
        print(Fore.RED + "Invalid format. Please use MM-YYYY." + Style.RESET_ALL)
        return

    total_expenses = 0
    category_totals = {}

    with open(EXPENSES_FILE, 'r') as file:
        next(file)  # Skip header
        for line in file:
            category, amount, date = line.strip().split(',')
            expense_date = datetime.strptime(date, "%Y-%m-%d")
            if expense_date.strftime("%m-%Y") == month_year:
                total_expenses += float(amount)
                if category not in category_totals:
                    category_totals[category] = 0
                category_totals[category] += float(amount)

    # Display summary
    print(Fore.CYAN + f"\nMonthly Summary ({month_year}):" + Style.RESET_ALL)
    print(Fore.GREEN + f"Total Expenses: {total_expenses}" + Style.RESET_ALL)
    print(Fore.MAGENTA + "By Category:" + Style.RESET_ALL)
    for category, total in category_totals.items():
        print(f"- {category}: {total}")

    export_summary_to_pdf(month_year, total_expenses, category_totals)

def export_summary_to_pdf(month_year, total_expenses, category_totals):
    print(Fore.YELLOW + "Generating PDF Report..." + Style.RESET_ALL)
    doc = SimpleDocTemplate(PDF_REPORT_FILE, pagesize=letter)
    elements = []

    # Add the title and generation date
    title = f"Expense Summary for {month_year}"
    current_date = datetime.now().strftime("%Y-%m-%d")
    header_data = [[title], [f"Generated on: {current_date}"]]
    header_table = Table(header_data)
    header_table.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 14),  # Title font size
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),  # Padding under title
        ("FONTSIZE", (0, 1), (-1, -1), 10),  # Date font size
    ]))
    elements.append(header_table)
    elements.append(Table([[""]]))  # Spacer

    # Create table data including date column
    data = [["Category", "Total Amount", "Generated Date"]]
    for category, total in category_totals.items():
        data.append([category, f"{total:.2f}", current_date])

    # Add total row
    data.append(["Total", f"{total_expenses:.2f}", ""])

    # Style and create the table
    table = Table(data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)
    doc.build(elements)
    print(Fore.GREEN + f"PDF Report generated: {PDF_REPORT_FILE}" + Style.RESET_ALL)

# Updated monthly_summary function with export option
def monthly_summary():
    print(Fore.BLUE + "\nMonthly Summary" + Style.RESET_ALL)
    month_year = input(Fore.YELLOW + "Enter month and year (MM-YYYY): " + Style.RESET_ALL).strip()
    try:
        datetime.strptime(month_year, "%m-%Y")  # Validate input
    except ValueError:
        print(Fore.RED + "Invalid format. Please use MM-YYYY." + Style.RESET_ALL)
        return

    total_expenses = 0
    category_totals = {}

    with open(EXPENSES_FILE, 'r') as file:
        next(file)  # Skip header
        for line in file:
            category, amount, date = line.strip().split(',')
            expense_date = datetime.strptime(date, "%Y-%m-%d")
            if expense_date.strftime("%m-%Y") == month_year:
                total_expenses += float(amount)
                if category not in category_totals:
                    category_totals[category] = 0
                category_totals[category] += float(amount)

    # Display summary in console
    print(Fore.CYAN + f"\nMonthly Summary ({month_year}):" + Style.RESET_ALL)
    print(Fore.GREEN + f"Total Expenses: {total_expenses}" + Style.RESET_ALL)
    print(Fore.MAGENTA + "By Category:" + Style.RESET_ALL)
    for category, total in category_totals.items():
        print(f"- {category}: {total:.2f}")

    # Prompt for PDF export
    export_option = input(Fore.BLUE + "\nDo you want to export the summary as a PDF? (yes/no): " + Style.RESET_ALL).strip().lower()
    if export_option in ("yes", "y"):
        export_summary_to_pdf(month_year, total_expenses, category_totals)

# Main menu
def main_menu():
    ensure_file()
    while True:
        print(Fore.CYAN + "\nWelcome to Personal Expense Tracker!" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. Add Expense" + Style.RESET_ALL)
        print(Fore.YELLOW + "2. View Expenses" + Style.RESET_ALL)
        print(Fore.YELLOW + "3. Monthly Summary" + Style.RESET_ALL)
        print(Fore.YELLOW + "4. Exit" + Style.RESET_ALL)
        choice = input(Fore.BLUE + "Enter your choice: " + Style.RESET_ALL).strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print(Fore.RED + "Exiting. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main_menu()
