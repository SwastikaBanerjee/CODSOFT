import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            raise ValueError
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Enter number 1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter number 2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

label_operation = tk.Label(root, text="Choose an operation:")
label_operation.pack()
operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")
operation_menu = tk.OptionMenu(root, operation_var, *operation_choices)
operation_menu.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()