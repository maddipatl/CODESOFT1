import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # Create a list to store contacts
        self.contacts = []

        # Create and set up GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets for contact details
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for actions
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        # Get values from entry widgets
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        # Validate input
        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required.")
            return

        # Create a new Contact object and add it to the list
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)

        # Clear entry widgets after adding contact
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
            return

        contact_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in self.contacts])
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number:")
        if not search_term:
            return

        results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                results.append(f"{contact.name}: {contact.phone}")

        if results:
            result_text = "\n".join(results)
            messagebox.showinfo("Search Results", result_text)
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

    def update_contact(self):
        search_term = simpledialog.askstring("Update", "Enter name or phone number:")
        if not search_term:
            return

        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                # Update contact details
                contact.name = simpledialog.askstring("Update", "Enter new name:", initialvalue=contact.name)
                contact.phone = simpledialog.askstring("Update", "Enter new phone number:", initialvalue=contact.phone)
                contact.email = simpledialog.askstring("Update", "Enter new email:", initialvalue=contact.email)
                contact.address = simpledialog.askstring("Update", "Enter new address:", initialvalue=contact.address)

                messagebox.showinfo("Success", "Contact updated successfully.")
                return

        messagebox.showinfo("Update", "Contact not found.")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete", "Enter name or phone number:")
        if not search_term:
            return

        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                # Remove the contact from the list
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully.")
                return

        messagebox.showinfo("Delete", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
