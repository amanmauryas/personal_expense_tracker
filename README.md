# **Personal Expense Tracker**

This Python application provides a command-line interface for tracking expenses, viewing summaries, and exporting detailed reports as PDF files.

---

## **Features**

- **Add an Expense**  
  Input details like category, amount, and date (YYYY-MM-DD) to save an expense.
  
- **View Expenses by Category**  
  Display all recorded expenses organized by category.

- **Monthly Summary**  
  Input a month and year to see total expenses for that period, categorized with subtotals.

- **Export Summary to PDF**  
  Generate and save a PDF containing the monthly expense summary with the totals and timestamp.

---

## **Code Overview**

### **Modules Used**
- `os`: For checking and creating files.  
- `datetime`: For validating and managing dates.  
- `colorama`: For colorful CLI output.  
- `reportlab`: For generating PDF reports.

### **Key Functions**

#### **`ensure_file()`**
Ensures that the expense tracking file (`expenses.txt`) exists. If not, it creates one with a header line.

#### **`add_expense()`**
Prompts the user to input expense details (category, amount, and date). The function validates the date format and saves the details into `expenses.txt`.  
**Example**:  
```plaintext
Enter category (e.g., Food, Travel): Travel  
Enter amount: 200  
Enter date (YYYY-MM-DD): 2024-12-24  
view_expenses()
Displays all recorded expenses grouped by their respective categories.

monthly_summary()
Asks for a month and year (MM-YYYY) and calculates total expenses within that period. Expenses are displayed by category with subtotals.

export_summary_to_pdf(month_year)
Takes a month-year as input.
Extracts relevant expense data from the file.
Generates a professionally formatted PDF using reportlab.
Saves the PDF with the filename format Expense_Summary_MM-YYYY.pdf.
Example Output PDF:

sql
Copy code
Title: Expense Summary  
Date Generated: [Current Date and Time]  

Category           Total Amount  
--------------------------------  
Food               150.00  
Travel             200.00  
Total Expenses:    350.00  
main_menu()
Provides the main interface with options to add expenses, view records, generate summaries, and export to PDF.

Options:

plaintext
Copy code
1. Add Expense  
2. View Expenses  
3. Monthly Summary  
4. Export Summary to PDF  
5. Exit  
Usage Instructions
Setup
Requirements
Install Python 3.6+
Install the required libraries:
bash
Copy code
pip install colorama reportlab
Run the Application
Run the script:

bash
Copy code
python expense_tracker.py
File Structure
expenses.txt: The app’s database for storing expense records.
Generated Files
PDF Report: Exported summaries will be saved in the same directory as Expense_Summary_MM-YYYY.pdf.
Planned Improvements
Add more interactive data views (e.g., yearly summaries).
Include graphs in the exported PDF.
Provide options to delete or edit specific expense entries.
