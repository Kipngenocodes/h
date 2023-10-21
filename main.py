import tkinter as tk
from tkinter import messagebox


# Function to assign work based on age
def assign_work():
    age = int(age_entry.get())

    if age < 18:
        work = "You are too young to work."
    elif age >= 18 and age < 30:
        work = "You are assigned as an intern."
    elif age >= 30 and age < 50:
        work = "You are assigned as a junior employee."
    else:
        work = "You are assigned as a senior employee."

    messagebox.showinfo("Work Assignment", work)


# Create the main window
window = tk.Tk()
window.title("Age and Work Assignment")

# Create and pack labels and entry fields
age_label = tk.Label(window, text="Enter your age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

# Create and pack the assign button
assign_button = tk.Button(window, text="Assign Work", command=assign_work)
assign_button.pack()

# Start the Tkinter main loop
window.mainloop()
