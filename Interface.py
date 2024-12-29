import pandas
import tkinter
from tkinter import *
from tkinter import messagebox
from BackEndExpenses import Expenses

window = Tk()
window.minsize(height=700, width=800)
window.title("Expenses")

expenses = Expenses()

display_label = Text(window)

#Creating a scrollbar
sb = Scrollbar(window, orient="vertical", command=display_label.yview)
display_label.config(yscrollcommand=sb.set)
sb.place(relx=1, rely=0, relheight=1, anchor="ne")
display_label.grid(row=0, rowspan=2, column=0, columnspan=2)

# A function to update data entered in various fields into a file
def upload():
    display_label.insert(1.0, END)

    # Cheacking if any of the fields are empty to maintain data consistency
    if len(day_input.get()) == 0:
        messagebox.showerror("Entry", "Enter Date")

    else :
        expenses.getdate = day_input.get()

    expenses.getmonth = menu_options.get()

    if len(expense_options.get()) == 0 or type_of_expense.get() == "TypeOfExpense":
        messagebox.showerror("Entry", "Enter Type")

    else :
        expenses.get_type_of = expense_options.get()

    if amount.get() == "EnterAmount" or len(amount.get()) == 0:
        messagebox.showerror("Entry", "Enter Amount")

    else :
        expenses.amount_to_write = amount.get()
    EntryBox()
    if len(day_input.get()) != 0 and expense_options.get() != "TypeOfExpense" and amount.get() != "EnterAmount":
        expenses.edit_File()
    expenses.read_File()

# A function to show data in a text label
def EntryBox():
    display_label.delete(1.0, END)
    expenses.getmonth = menu_options.get()
    try :
        with open(f"Expenses  - {expenses.getmonth} 2024.csv", 'r') as file_data:
            csv_file = pandas.read_csv(file_data, index_col="Date")
            display_label.insert(END, f"{csv_file}")
    except FileNotFoundError:
        messagebox.showerror("Entry", "File Doesnt exist, creating new file")
        expenses.create_File()
def main_plot():
    expenses.getmonth = menu_options.get()
    expenses.plot()


month = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]

day_input = Entry()
day_input.grid(row = 2, column = 0, padx = 10, pady = 10)

menu_options = tkinter.StringVar()
month_menu = OptionMenu(window, menu_options, *month)
month_menu.grid(row = 2, column = 1, padx = 10, pady = 10)

year_label =  Label(window, text="2024")
year_label.grid(row = 2, column = 2, padx = 10, pady = 10)

type_of_expense = ["Groceries", "College", "Dentist", "Misc", "Outings", "Food", "Meds"]
expense_options = tkinter.StringVar()
expense_menu = OptionMenu(window, expense_options, *type_of_expense)
expense_menu.grid(row = 3, column = 0, columnspan = 1, padx = 10, pady =10)

amount = Entry()
amount.grid(row = 3, column = 2, columnspan = 1, padx = 10, pady =10)
amount.insert(END, "EnterAmount")

submit_button = Button(window, text="SUBMIT", command = upload)
submit_button.grid(row = 4, column = 1, padx = 10, pady = 10)

show_button =Button(window, text = "SHOW", command= EntryBox)
show_button.grid(row = 4, column = 2, padx = 10, pady = 10)

plot_button = Button(window, text="PLOT", command = main_plot)
plot_button.grid(row= 5, column = 1, padx = 10, pady =10)

window.mainloop()

