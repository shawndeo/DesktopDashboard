import tkinter as tk
from tkinter import
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady = 10)

        self.task_entry = tk.Entry(self.frame,
                                   width = 35)
        self.task_entry.pack(side = tk.LEFT,
                             padx = 10)
        
        self.add_task_button = tk.Button(self.frame,
                                         text = "Add Task",
                                         command = self.add_task)
        self.add_task_button.pack(side = tk.LEFT)

        self.task_listbox = tk.Listbox(root,
                                       width = 50,
                                       height = 15)
        self.task_listbox.pack(pady = 10)

        self.delete_task_button = tk.Button(root,
                                            text = "Delete Task",
                                            command = self.delete_task)
        self.delete_task_button.pack(pady = 5)

        self.clear_tasks_button = tk.Button(root,
                                            text = "Clear All Tasks",
                                            command = self.clear_tasks)
        self.clear_tasks_button.pack(pady = 5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0,
                                   tk.END)
        else:
            messagebox.showwarning("Warning",
                                   "You must enter a task!")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning",
                                   "You must select a task.")
        
    def clear_tasks(self):
        self.tasks.clear()
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0,
                                 tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END,
                                     task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

