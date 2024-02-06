import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please Select a task to delete.")

#Create main window

# Create a new Tkinter window
window = tk.Tk()

# Set the title of the window
window.title("To-Do List")

#Create the task entry
entry_task = tk.Entry(window, width = 50)
entry_task.pack(padx = 10, pady=10)

#Create the add button
btn_add = tk.Button(window, text="Add Task", width=48, command= add_task)
btn_add.pack(padx=10, pady=10)

#Create task list
listbox_tasks = tk.Listbox(window, height=10, width=50)
listbox_tasks.pack(padx=10, pady=10)

#Create delete button 
btn_delete = tk.Button(window, text="Delete Task", width=48, command=delete_task)
btn_delete.pack(padx=10, pady=5)

# Start the Tkinter event loop
window.mainloop()
