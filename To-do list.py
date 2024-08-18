import tkinter as tk
from tkinter import messagebox, simpledialog, Text
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        self.root.configure(bg="#f7f7f7")

        self.tasks = []

        # Header
        header = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="#333")
        header.pack(pady=10)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, height=12, width=50, selectmode=tk.SINGLE, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root, bg="#f7f7f7")
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Add Task", command=self.add_task, width=12, bg="blue"
                                                                                                       "", fg="white", font=("Helvetica", 10, "bold"))
        self.add_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, width=12, bg="red", fg="white", font=("Helvetica", 10, "bold"))
        self.delete_button.grid(row=0, column=1, padx=5)

        self.update_button = tk.Button(button_frame, text="Update Task", command=self.update_task, width=12, bg="pink", fg="white", font=("Helvetica", 10, "bold"))
        self.update_button.grid(row=0, column=2, padx=5)

        self.view_button = tk.Button(button_frame, text="View Task Details", command=self.view_task, width=12, bg="green", fg="white", font=("Helvetica", 10, "bold"))
        self.view_button.grid(row=1, column=1, pady=5)

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        if title:
            description = simpledialog.askstring("Add Task", "Enter task description:")
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task = {"title": title, "description": description, "date_time": date_time}
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, f"{title} (Added on: {date_time})")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            confirm = messagebox.askyesno("Delete Task", f"Are you sure you want to delete '{self.tasks[selected_task_index[0]]['title']}'?")
            if confirm:
                self.tasks.pop(selected_task_index[0])
                self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            updated_title = simpledialog.askstring("Update Task", "Update the title:", initialvalue=task["title"])
            updated_description = simpledialog.askstring("Update Task", "Update the description:", initialvalue=task["description"])
            if updated_title and updated_description:
                self.tasks[selected_task_index[0]] = {"title": updated_title, "description": updated_description, "date_time": task["date_time"]}
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, f"{updated_title} (Added on: {task['date_time']})")
        else:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def view_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            task_details = f"Title: {task['title']}\nDescription: {task['description']}\nAdded on: {task['date_time']}"
            messagebox.showinfo("Task Details", task_details)
        else:
            messagebox.showwarning("View Task", "Please select a task to view details.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
