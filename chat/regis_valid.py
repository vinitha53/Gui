import tkinter as tk
from tkinter import messagebox
import re

# Function to validate email
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Function to handle form submission
def register_user():
    username = entry_username.get()
    email = entry_email.get()
    phone = entry_phone.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # Basic validation
    if not username or not email or not phone or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required")
        return

    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "Phone number must be 10 digits")
        return

    if not is_valid_email(email):
        messagebox.showerror("Error", "Invalid email address")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # Here, you could add code to save the data to a database or file
    # For now, we'll just show a success message
    messagebox.showinfo("Success", "Registration Successful")

    # Clear the form fields
    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_confirm_password.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x300")

# Create and place labels and entry widgets
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

label_phone = tk.Label(root, text="Phone Number:")
label_phone.pack(pady=5)
entry_phone = tk.Entry(root)
entry_phone.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

label_confirm_password = tk.Label(root, text="Confirm Password:")
label_confirm_password.pack(pady=5)
entry_confirm_password = tk.Entry(root, show="*")
entry_confirm_password.pack(pady=5)

# Create and place the register button
button_register = tk.Button(root, text="Register", command=register_user)
button_register.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
