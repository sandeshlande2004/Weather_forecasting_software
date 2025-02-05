import tkinter as tk
from tkinter import messagebox

def calculate_emi(principal, annual_interest_rate, period_in_months):
    monthly_interest_rate = annual_interest_rate / (12 * 100)  # Convert to monthly and decimal
    emi = principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** period_in_months) / ((1 + monthly_interest_rate) ** period_in_months - 1)
    return emi

def calculate():
    try:
        principal = float(principal_entry.get())
        interest_rate = float(interest_rate_entry.get())
        period = int(period_entry.get())
        emi = calculate_emi(principal, interest_rate, period)
        emi_label.config(text=f"EMI: {emi:.2f} Rs")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for all fields")

root = tk.Tk()
root.title("EMI Calculator")

principal_label = tk.Label(root, text="Loan Amount in Rs:")
principal_label.pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

interest_rate_label = tk.Label(root, text="Interest Rate in % p.a.:")
interest_rate_label.pack()
interest_rate_entry = tk.Entry(root)
interest_rate_entry.pack()

period_label = tk.Label(root, text="Period (in months):")
period_label.pack()
period_entry = tk.Entry(root)
period_entry.pack()

calculate_button = tk.Button(root, text="Calculate EMI", command=calculate)
calculate_button.pack()

emi_label = tk.Label(root, text="")
emi_label.pack()

root.mainloop()
