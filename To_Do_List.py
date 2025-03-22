import tkinter as tk
from tkinter import messagebox
import json

class TagGoalToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("TagGoal - To-Do List")
        self.root.geometry("500x500")

        self.task_list = []
        self.selected_task = None

        header = tk.Label(self.root, text="TagGoal", font=("Arial", 14, "bold"), bg="gray", fg="black")
        header.pack(fill=tk.X)

        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        self.add_button = tk.Button(top_frame, text="+", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.task_entry = tk.Entry(top_frame, width=20, fg="gray")
        self.task_entry.insert(0, "New Target")
        self.task_entry.bind("<FocusIn>", self.clear_hint)
        self.task_entry.bind("<FocusOut>", self.add_hint)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.date_entry = tk.Entry(top_frame, width=15, fg="gray")
        self.date_entry.insert(0, "Last Date")
        self.date_entry.bind("<FocusIn>", self.clear_date_hint)
        self.date_entry.bind("<FocusOut>", self.add_date_hint)
        self.date_entry.pack(side=tk.LEFT, padx=5)

        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.desc_frame = tk.Frame(self.root, bg="lightgray")
        self.desc_frame.pack(fill=tk.X, padx=10, pady=5)
        self.desc_frame.pack_forget()

        self.desc_label = tk.Label(self.desc_frame, text="Description:", bg="lightgray")
        self.desc_label.pack(anchor="w", padx=5, pady=2)

        self.desc_text = tk.Text(self.desc_frame, height=4, width=50)
        self.desc_text.pack(padx=5, pady=5)

        self.save_desc_button = tk.Button(self.desc_frame, text="Save", command=self.save_description)
        self.save_desc_button.pack(pady=5)

        self.load_tasks()

    def clear_hint(self, event):
        if self.task_entry.get() == "New Target":
            self.task_entry.delete(0, tk.END)
            self.task_entry.config(fg="black")

    def add_hint(self, event):
        if not self.task_entry.get():
            self.task_entry.insert(0, "New Target")
            self.task_entry.config(fg="gray")

    def clear_date_hint(self, event):
        if self.date_entry.get() == "Last Date":
            self.date_entry.delete(0, tk.END)
            self.date_entry.config(fg="black")

    def add_date_hint(self, event):
        if not self.date_entry.get():
            self.date_entry.insert(0, "Last Date")
            self.date_entry.config(fg="gray")

    def add_task(self):
        task_name = self.task_entry.get().strip()
        last_date = self.date_entry.get().strip()

        if task_name and task_name != "New Target" and last_date and last_date != "Last Date":
            self.add_task_to_ui(task_name, last_date)
            self.task_list.append({"name": task_name, "date": last_date, "description": ""})
            self.save_tasks() 
            self.task_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both a target and a last date!")

    def add_task_to_ui(self, task_name, last_date):
        task_frame = tk.Frame(self.task_frame, bg="lightgray", padx=5, pady=5)
        task_frame.pack(fill=tk.X, pady=2)

        task_label = tk.Label(task_frame, text=task_name, anchor="w", bg="lightgray", cursor="hand2")
        task_label.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        task_label.bind("<Button-1>", lambda e: self.show_description(task_name))

        date_label = tk.Label(task_frame, text=last_date, bg="lightgray")
        date_label.pack(side=tk.RIGHT, padx=5)

        delete_button = tk.Button(task_frame, text="Delete", command=lambda: self.delete_task(task_frame, task_name))
        delete_button.pack(side=tk.RIGHT, padx=5)

    def show_description(self, task_name):
        for task in self.task_list:
            if task["name"] == task_name:
                self.selected_task = task
                self.desc_text.delete("1.0", tk.END)
                self.desc_text.insert(tk.END, task["description"])
                self.desc_frame.pack(fill=tk.X, padx=10, pady=5)
                return

    def save_description(self):
        if self.selected_task:
            new_desc = self.desc_text.get("1.0", tk.END).strip()
            self.selected_task["description"] = new_desc
            self.save_tasks()
            messagebox.showinfo("Success", "Description updated successfully!")

    def delete_task(self, task_frame, task_name):
        task_frame.destroy()
        self.task_list = [task for task in self.task_list if task["name"] != task_name]
        self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            json.dump(self.task_list, f)

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.task_list = json.load(f)
                for task in self.task_list:
                    self.add_task_to_ui(task["name"], task["date"])
        except FileNotFoundError:
            self.task_list = []  
        except json.JSONDecodeError:
            self.task_list = []  

if __name__ == "__main__":
    root = tk.Tk()
    app = TagGoalToDo(root)
    root.mainloop()
