import tkinter as tk


# Function to assign work based on age
def assign_work():
    age = int(age_entry.get())
    if age < 18:
        work = "Student"
        text_color = "blue"
    elif age < 30:
        work = "Junior"
        text_color = "green"
    elif age < 50:
        work = "Mid-level"
        text_color = "orange"
    else:
        work = "Senior"
        text_color = "red"

    work_label.config(text=f"Work: {work}", fg=text_color)


# Create the tkinter window
window = tk.Tk()
window.title("Work Assignment")

# Create labels and entry widget
age_label = tk.Label(window, text="Enter Age:")
age_label.pack()

# having age entry widget
age_entry = tk.Entry(window)
age_entry.pack()

work_label = tk.Label(window, text="Work: ", font=("Arial", 12))
work_label.pack()

# Create a button to assign work
assign_button = tk.Button(window, text="Assign Work", command=assign_work)
assign_button.pack()

# Run the tkinter main loop
window.mainloop()
