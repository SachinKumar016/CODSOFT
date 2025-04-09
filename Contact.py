import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

class ContactManager:
    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()
        if name and phone and email and address:
            self.contacts.append([name, phone, email, address])
            self.save_contacts()
            self.update_contact_list()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "All fields are required!")
    def update_contact_list(self):
        self.contact_table.delete(*self.contact_table.get_children())
        for contact in self.contacts:
            self.contact_table.insert("", tk.END, values=contact)
    def search_contact(self):
        query = self.search_entry.get().strip().lower()
        self.contact_table.delete(*self.contact_table.get_children())
        for contact in self.contacts:
            if query in contact[0].lower() or query in contact[1]:
                self.contact_table.insert("", tk.END, values=contact)
    def save_contacts(self):
        with open("contacts.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Address"])
            writer.writerows(self.contacts)
    def load_contacts(self):
        if os.path.exists("contacts.csv"):
            with open("contacts.csv", "r") as file:
                reader = csv.reader(file)
                next(reader, None)
                self.contacts = [row for row in reader]
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
    def delete_contact(self):
        selected_item = self.contact_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No contact selected!")
            return   
        contact_values = self.contact_table.item(selected_item, "values")
        self.contacts = [contact for contact in self.contacts if contact[0] != contact_values[0]]
        self.save_contacts()
        self.update_contact_list()
    def update_contact(self):
        selected_item = self.contact_table.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No contact selected!")
            return
        contact_values = self.contact_table.item(selected_item, "values")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)   
        self.name_entry.insert(0, contact_values[0])
        self.phone_entry.insert(0, contact_values[1])
        self.email_entry.insert(0, contact_values[2])
        self.address_entry.insert(0, contact_values[3])
        self.contacts = [contact for contact in self.contacts if contact[0] != contact_values[0]]
        self.save_contacts()
        self.update_contact_list()
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("1100x550")
        self.contacts = []
        self.load_contacts()
        tk.Label(self.root, text="Contact Manager", font=("Arial", 14, "bold")).pack(pady=5)
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=5)
        tk.Label(self.frame, text="Name:").grid(row=0, column=0, padx=5, pady=2)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=2)
        tk.Label(self.frame, text="Phone:").grid(row=1, column=0, padx=5, pady=2)
        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=2)
        tk.Label(self.frame, text="Email:").grid(row=2, column=0, padx=5, pady=2)
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=2)
        tk.Label(self.frame, text="Address:").grid(row=3, column=0, padx=5, pady=2)
        self.address_entry = tk.Entry(self.frame)
        self.address_entry.grid(row=3, column=1, padx=5, pady=2)
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)
        self.search_entry = tk.Entry(self.root, width=30)
        self.search_entry.pack(pady=5)
        self.search_button = tk.Button(self.root, text="Search", command=self.search_contact)
        self.search_button.pack(pady=5)
        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(pady=5)
        self.contact_table = ttk.Treeview(self.table_frame, columns=("Name", "Phone", "Email", "Address", "Actions"), show="headings")
        self.contact_table.heading("Name", text="Name")
        self.contact_table.heading("Phone", text="Phone")
        self.contact_table.heading("Email", text="Email")
        self.contact_table.heading("Address", text="Address")
        self.contact_table.pack()
        self.update_contact_list()
        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)
        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

root = tk.Tk()
app = ContactManager(root)
root.mainloop()