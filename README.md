# Personal Expense Tracker

## Project Description
The **Personal Expense Tracker** is a Python-based application designed to help users efficiently track and manage their personal expenses. Users can add daily expenses, view their expenses by category, and get a monthly summary to analyze their spending habits.

The application uses a text file (`expenses.txt`) to store expense data, ensuring persistence across sessions. The console-based interface is enhanced with color-coded outputs for better usability and readability.

---

## Features Implemented
- **Add Expense**
  - Input expense details: category, amount, and date.
  - Validate date input format.
  - Persist expense data into a text file.

- **View Expenses by Category**
  - Categorize and display expenses stored in the file.
  - Show a breakdown of amounts and dates for each category.

- **Monthly Summary**
  - Summarize total expenses and a category-wise breakdown for a specific month.
  - Provide insights into monthly spending.

- **Export as pdf**
  - Summaries can be exported as pdf in a well-designed format
  - 
- **User-Friendly Console Interface**
  - Includes colored prompts and messages using `colorama` for better readability.

---

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amanmauryas/personal_expense_tracker
   cd personal_expense_tracker
   ```

2. **Ensure Python is Installed**:
   - Required version: Python 3.6 or later.
   - To check, run:
     ```bash
     python --version
     ```

3. **Install Dependencies**:
   - Use pip to install the required `colorama` and reportlab library:
     ```bash
     pip install colorama reportlab
     ```

4. **Run the Application**:
   ```bash
   python expense_tracker.py
   ```

---

## Usage Instructions

1. **Main Menu**:
   - Run the program to view the main menu with the following options:
     ```
     Welcome to Personal Expense Tracker!
     1. Add Expense
     2. View Expenses
     3. Monthly Summary
     4. Exit
     ```

2. **Add Expense**:
   - Select option `1` and enter the requested details.
   - Example:
     ```
     Enter category (e.g., Food, Travel): Food
     Enter amount: 200
     Enter date (YYYY-MM-DD): 2024-12-24
     Expense added successfully!
     ```

3. **View Expenses**:
   - Select option `2` to see expenses categorized.
   - Example output:
     ```
     Expenses:

     Food:
     - Amount: 200 - Date: 2024-12-24

     Travel:
     No expenses recorded.
     ```

4. **Monthly Summary**:
   - Select option `3` and input the desired month and year in `MM-YYYY` format.
   - Example output:
     ```
     Monthly Summary (12-2024):
     Total Expenses: 200
     By Category:
     - Food: 200
     ```
   - This will ask a question *Do you want to export the summary as a PDF? (yes/no):* to export as pdf
   - sample format of exported pdf
   - ![image](https://github.com/user-attachments/assets/fbb9d7d4-ac77-4b51-9f8e-0c078016e6a8)

5. **Exit**:
   - Select option `4` to exit the application.

---

## Instructions for Installation

1. **Dependencies**:
   - Ensure you have Python 3 installed.
   - Install the `colorama` and `reportlab` library by running:
     ```bash
     pip install colorama reportlab
     ```

2. **File Setup**:
   - The program automatically creates the `expenses.txt` file in the current directory if it does not exist.
   - If you have opted for pdf `expense_summary.pdf` file will be created in the current directory.

---

## Notes
- All expenses are stored in `expenses.txt` in the following format:
  ```
  Category,Amount,Date
  Food,200,2024-12-24
  Travel,150,2024-12-23
  ```

- Ensure the file `expenses.txt` is located in the same directory as the script for proper functionality.

- Use valid date formats (YYYY-MM-DD) for adding expenses and (MM-YYYY) for monthly summaries.

---

## Future Enhancements
- Enhanced filtering options by week or custom date range.
- Support for graphical summaries (e.g., pie charts or bar graphs).

