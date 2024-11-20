import os
import random
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be greater than zero.")
        
        # Characters to use for password
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
        
        # Generate password
        password = "".join(random.choice(characters) for _ in range(length))
        
        # Display password
        result_label.config(text=f"Generated Password: {password}")
        
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Setting up the GUI
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.configure(bg="#add8e6")  # Light blue background

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#add8e6")
title_label.pack(pady=10)

# Length Input
length_frame = tk.Frame(root, bg="#add8e6")
length_frame.pack(pady=10)
length_label = tk.Label(length_frame, text="Enter password length:", font=("Arial", 12), bg="#add8e6")
length_label.pack(side="left", padx=5)
length_entry = tk.Entry(length_frame, width=10, font=("Arial", 12))
length_entry.pack(side="left")

# Generate Button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_password)
generate_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#add8e6")
result_label.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Generated passwords are not stored.", font=("Arial", 10), bg="#add8e6")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
