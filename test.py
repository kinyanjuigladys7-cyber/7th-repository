import tkinter as tk
from tkinter import messagebox

# Calculate BMI
def calculate():
    age = int(age_entry.get())
    height = float(height_entry.get())
    weight = float(weight_entry.get())

    bmi = weight / (height * height)

    result.config(text="BMI = " + str(round(bmi, 2)))


# Window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x500")

# Title
tk.Label(
    window,
    text="BMI Calculator",
    font=("Arial", 16, "bold"),
    bg="green",
    fg="white"
).pack(fill="x", pady=20)

# Gender frame
gender_frame = tk.Frame(window)
gender_frame.pack(pady=10)

gender = tk.StringVar()
gender.set("Male")

# Male box
male_box = tk.Radiobutton(
    gender_frame,
    text="Male",
    variable=gender,
    value="Male",
    width=12,
    height=2,
    indicatoron=False
)
male_box.pack(side="left", padx=10)

# Female box
female_box = tk.Radiobutton(
    gender_frame,
    text="Female",
    variable=gender,
    value="Female",
    width=12,
    height=2,
    indicatoron=False
)
female_box.pack(side="left", padx=10)

# Units
tk.Label(
    window,
    text="Units",
    font=("Arial", 12, "bold")
).pack(pady=10)

unit_frame = tk.Frame(window)
unit_frame.pack(pady=10)

unit = tk.StringVar()
unit.set("Metric")

# Imperial - LEFT
tk.Radiobutton(
    unit_frame,
    text="Imperial\n(lbs, ft)",
    variable=unit,
    value="Imperial",
    width=12,
    height=2,
    indicatoron=False
).pack(side="left", padx=10)

# Metric - RIGHT
tk.Radiobutton(
    unit_frame,
    text="Metric\n(kg, cm)",
    variable=unit,
    value="Metric",
    width=12,
    height=2,
    indicatoron=False
).pack(side="left", padx=10)



# Age
tk.Label(window, text="Age").pack()
age_entry = tk.Entry(window)
age_entry.pack(pady=5)

# Height
tk.Label(window, text="Height (metres)").pack()
height_entry = tk.Entry(window)
height_entry.pack(pady=5)

# Weight
tk.Label(window, text="Weight (kg)").pack()
weight_entry = tk.Entry(window)
weight_entry.pack(pady=5)

# Button
tk.Button(
    window,
    text="Calculate BMI",
    command=calculate,
    bg="green",
    fg="white"
).pack(pady=20)

# Result
result = tk.Label(
    window,
    text="YOUR BMI will appear here",
    font=("Arial", 14)
)
result.pack(pady=20)

# Run
window.mainloop()