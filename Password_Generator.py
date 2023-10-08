import tkinter as tk
import random
import string

def generate_password():
    try:
        name = name_entry.get()
        password_length = int(length_entry.get())
        if password_length <= 0:
            raise ValueError
        password_characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))
        password_label.config(text=f"Hello, {name}! Your Generated Password: {generated_password}")
    except ValueError:
        password_label.config(text="Please enter a valid password length.")

root = tk.Tk()
root.title("Password Generator")

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="", font=("Arial", 12))
password_label.pack()

root.mainloop()