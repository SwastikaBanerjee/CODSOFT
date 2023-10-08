import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def edit_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        updated_task = task_entry.get()
        if updated_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300") 

bg_color = "#EFEFEF" 
button_color = "#4CAF50" 
button_text_color = "white"
entry_bg_color = "white"

task_entry = tk.Entry(root, width=40, bg=entry_bg_color)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg=button_color, fg=button_text_color)
add_button.pack()

edit_button = tk.Button(root, text="Edit Task", command=edit_task, bg=button_color, fg=button_text_color)
edit_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg=button_color, fg=button_text_color)
delete_button.pack()

task_listbox = tk.Listbox(root, width=40, bg=entry_bg_color)
task_listbox.pack()

root.mainloop()