from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector

class BankManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank Management System")
        self.master.geometry("400x200")

        self.balance = 0

        self.label_balance = Label(self.master, text="Balance: $0")
        self.label_balance.pack()

        self.label_amount = Label(self.master, text="Amount:")
        self.label_amount.pack()

        self.entry_amount = Entry(self.master)
        self.entry_amount.pack()

        self.button_deposit = Button(self.master, text="Deposit", command=self.deposit)
        self.button_deposit.pack(side=LEFT)

        self.button_withdraw = Button(self.master, text="Withdraw", command=self.withdraw)
        self.button_withdraw.pack(side=LEFT)

    def update_balance_label(self):
        self.label_balance.config(text="Balance: $" + str(self.balance))

    def deposit(self):
        amount = self.entry_amount.get()
        if amount.isdigit() and int(amount) > 0:
            self.balance += int(amount)
            self.update_balance_label()
            messagebox.showinfo("Success", "Amount deposited successfully.")
        else:
            messagebox.showerror("Error", "Invalid amount.")

    def withdraw(self):
        amount = self.entry_amount.get()
        if amount.isdigit() and int(amount) > 0:
            if int(amount) <= self.balance:
                self.balance -= int(amount)
                self.update_balance_label()
                messagebox.showinfo("Success", "Amount withdrawn successfully.")
            else:
                messagebox.showerror("Error", "Insufficient funds.")
        else:
            messagebox.showerror("Error", "Invalid amount.")

def main():
    root = Tk()
    bank_system = BankManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
