import csv
import pandas
from tkinter import messagebox
import matplotlib.pyplot as plt

class Expenses :
    def __init__(self):
        self.date = []
        self.getdate = ""

        self.type_of_expense = []
        self.get_type_of = ""

        self.amount = []
        self.amount_to_write = ""

        self.month = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06",
                      "July": "07","August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}
        self.getmonth = ""
        self.getmonth_towrite()

    # To calculate the month number from the name of the month, using the above dictionary.
    def getmonth_towrite(self):
        for m in self.month:
            if m == self.getmonth:
                return self.month[m]
    # Creates a file if doesnt exist
    def create_File(self):
        with open(f"Expenses  - {self.getmonth} 2024.csv", 'w') as data:
            data.write("Date,Type,Amount\n")

    # Reads a file to get various data from it which then can be used to update/edit that particular data,
    # feature yet to be implemented
    def read_File(self):

        try :
            with open(f"Expenses  - {self.getmonth} 2024.csv", "r") as data_file:
                csv_file = pandas.read_csv(data_file)
                graph_file = csv.reader(data_file)
                next(graph_file)
                for lines in graph_file:
                    self.date.append(lines[0])
                    self.type_of_expense.append(lines[1])
                    self.amount.append(lines[2])


        except FileNotFoundError:
            messagebox.showerror("Entry", "File doesnt exist, creating new file")
            self.create_File()

    # Editing the file using the various inputs gotten from the GUI window
    def edit_File(self):
            try :
                with open(f"Expenses  - {self.getmonth} 2024.csv", "a") as data:
                    data.write(f"\n{self.getdate}/{self.getmonth_towrite()}/2024,{self.get_type_of},{self.amount_to_write}")
            except FileNotFoundError:
                messagebox.showerror("Entry", "File doesnt exist, creating new file")
                self.create_File()

    # A function to plot the graph
    def plot(self):
        # If plt.close isnt invoked then the old plotted graph gets overwritten,
        plt.close()

        with open(f"Expenses  - {self.getmonth} 2024.csv", "r") as data_file:

            graph_file = csv.reader(data_file)
            next(graph_file)
            self.date = []
            self.amount = []
            self.type_of_expense = []
            for lines in graph_file:
                self.date.append(lines[0].split('/')[0])
                self.type_of_expense.append(lines[1])
                self.amount.append(lines[2])
        self.new_amount = []
        self.new_amount = list(map(float, self.amount))
        fig = plt.figure()
        plt.plot(self.date, self.new_amount)
        plt.show()




