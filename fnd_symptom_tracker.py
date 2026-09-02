import tkinter as tk
from tkinter import messagebox
import pandas as pd
import json
from datetime import datetime

# Function to save data
def save_data():
    date = datetime.now().strftime("%Y-%m-%d")
    comments = comments_entry.get("1.0", tk.END).strip()
    symptoms_data = {}
    for symptom, scale in zip(symptoms, scales):
        if scale.get() is not None:
            symptoms_data[symptom] = scale.get()
    data = {
        "Date": date,
        "Comments": comments,
        "Symptoms": symptoms_data
    }
    df = pd.DataFrame([data])
    try:
        with open('/home/yourusername/Desktop/fnd_symptoms.json', 'a') as f:  # Change this path to your desired directory
            df.to_json(f, lines=True)
        messagebox.showinfo("Success", "Data saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to load data
def load_data():
    try:
        with open('/home/yourusername/Desktop/fnd_symptoms.json', 'r') as f:  # Change this path to your desired directory
            data = pd.read_json(f, lines=True)
            for index, row in data.iterrows():
                date_entry.delete(0, tk.END)
                date_entry.insert(tk.END, row['Date'])
                comments_entry.delete("1.0", tk.END)
                comments_entry.insert("1.0", row['Comments'])
                for symptom_var, scale in zip(symptom_vars, scales):
                    if symptom in row['Symptoms']:
                        symptom_var.set(True)
                        scale.set(row['Symptoms'][symptom])
        messagebox.showinfo("Success", "Data loaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("FND Symptom Tracker")
root.configure(bg="#f0f8ff")  # Light blue background

# Create a canvas with scrollbars
canvas = tk.Canvas(root, bg="#ffffff", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a frame inside the canvas to hold all widgets
inner_frame = tk.Frame(canvas, bg="#f0f8ff")
canvas.create_window((0, 0), window=inner_frame, anchor="nw", tags="inner_frame")

# Style for bold text
bold_font = ("Helvetica", 12, "bold")

# Date input
date_label = tk.Label(inner_frame, text="Date:", font=bold_font, bg="#f0f8ff", fg="#000000")
date_label.grid(row=0, column=0, padx=10, pady=5)
date_entry = tk.Entry(inner_frame, bg="#ffffff", fg="#000000")
date_entry.grid(row=0, column=1, padx=10, pady=5)

# Comments box
comments_label = tk.Label(inner_frame, text="Comments:", font=bold_font, bg="#f0f8ff", fg="#000000")
comments_label.grid(row=2, column=0, padx=10, pady=5)
comments_entry = tk.Text(inner_frame, height=4, width=30, bg="#ffffff", fg="#000000")
comments_entry.grid(row=2, column=1, padx=10, pady=5)

# Symptom checkboxes and scales
symptoms = [
    "Tremor",
    "Seizures",
    "Dizziness",
    "Headache",
    "Numbness",
    "Weakness",
    "Difficulty walking",
    "Blurred vision",
    "Anxiety",
    "Brain fog"
]

symptom_vars = []
scales = []

for i, symptom in enumerate(symptoms):
    var = tk.BooleanVar()
    cb = tk.Checkbutton(inner_frame, text=symptom, variable=var, font=bold_font, bg="#f0f8ff", fg="#000000")
    cb.grid(row=i+3, column=0, padx=10, pady=5)
    symptom_vars.append(var)

    scale_label = tk.Label(inner_frame, text=f"{symptom} (1-10):", font=bold_font, bg="#f0f8ff", fg="#000000")
    scale_label.grid(row=i+3, column=1, padx=10, pady=5)
    scale = tk.Scale(inner_frame, from_=1, to=10, orient=tk.HORIZONTAL, length=200, bg="#ffffff", fg="#000000", troughcolor="#808080")
    scale.grid(row=i+3, column=2, padx=10, pady=5)
    scales.append(scale)

# Buttons
save_button = tk.Button(inner_frame, text="Save", command=save_data, font=bold_font, bg="#4CAF50", fg="#ffffff")
save_button.grid(row=len(symptoms)+8, column=0, padx=10, pady=5)

load_button = tk.Button(inner_frame, text="Load", command=load_data, font=bold_font, bg="#FF5733", fg="#ffffff")
load_button.grid(row=len(symptoms)+8, column=1, padx=10, pady=5)

# Auto-add current date
date_entry.insert(tk.END, datetime.now().strftime("%Y-%m-%d"))

# Configure inner_frame to fill the canvas
inner_frame.update_idletasks()
canvas.config(scrollregion=(0, 0, inner_frame.winfo_width(), inner_frame.winfo_height()))

# Run the main loop
root.mainloop()
