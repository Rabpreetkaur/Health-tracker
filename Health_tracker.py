import tkinter as tk
from tkinter import messagebox
import csv
import os

# File to store health data
FILE_NAME = "health_data.csv"

# Check if file exists, if not, create it with headers
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Weight (kg)", "Water Intake (L)", "Exercise (min)"])

# Function to save data
def save_data():
    date = date_entry.get()
    weight = weight_entry.get()
    water = water_entry.get()
    exercise = exercise_entry.get()
    
    if not (date and weight and water and exercise):
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, weight, water, exercise])
    
    messagebox.showinfo("Success", "Data Saved Successfully!")
    clear_entries()

# Function to clear entry fields
def clear_entries():
    date_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    water_entry.delete(0, tk.END)
    exercise_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Health Tracker")
root.geometry("300x250")

tk.Label(root, text="Date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Water Intake (L):").pack()
water_entry = tk.Entry(root)
water_entry.pack()

tk.Label(root, text="Exercise (min):").pack()
exercise_entry = tk.Entry(root)
exercise_entry.pack()

tk.Button(root, text="Save Data", command=save_data).pack(pady=5)
tk.Button(root, text="Clear", command=clear_entries).pack()

root.mainloop()
