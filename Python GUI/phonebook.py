import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

FILE_NAME = "contacts.xlsx"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            df = pd.read_excel(FILE_NAME)
            for _, row in df.iterrows():
                contacts_listbox.insert(tk.END, f"{row['Name']}: {row['Phone']}")
        except Exception as e:
            messagebox.showwarning("Грешка", f"Проблем при зареждане на контактите: {e}")


def save_contacts():
    contacts = contacts_listbox.get(0, tk.END)
    data = [contact.split(": ") for contact in contacts]
    df = pd.DataFrame(data, columns=["Name", "Phone"])
    df.to_excel(FILE_NAME, index=False)


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        if phone.isdigit() and len(phone) == 10:
            contacts_listbox.insert(tk.END, f"{name}: {phone}")
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            save_contacts()
        else:
            messagebox.showwarning("Грешка", "Моля, въведете валиден телефонен номер!")
    else:
        messagebox.showwarning("Грешка", "Моля, въведете име и телефонен номер!")


def delete_contact():
    selected = contacts_listbox.curselection()
    if selected:
        contact = contacts_listbox.get(selected[0])
        contacts_listbox.delete(selected)

        if os.path.exists(FILE_NAME):
            df = pd.read_excel(FILE_NAME)
            df = df[df.apply(lambda row: f"{row['ИМЕ']}: {row['ТЕЛ. НОМЕР']}" != contact, axis=1)]
            df.to_excel(FILE_NAME, index=False)
    else:
        messagebox.showwarning("Грешка", "Моля, изберете контакт за изтриване!")


root = tk.Tk()
root.title("Телефонен указател")

name_label = tk.Label(root, text="Име:")
name_label.grid(row=1, column=1)
name_entry = tk.Entry(root)
name_entry.grid(row=2, column=1)

phone_label = tk.Label(root, text="Телефон:")
phone_label.grid(row=3, column=1)
phone_entry = tk.Entry(root)
phone_entry.grid(row=4, column=1)

add_button = tk.Button(root, text="Добави контакт", command=add_contact)
add_button.grid(row=5, column=1)

contacts_listbox = tk.Listbox(root, width=40)
contacts_listbox.grid(row=6, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Изтрий контакт", command=delete_contact)
delete_button.grid(row=7, column=1, padx=5, pady=5)

load_contacts()

root.mainloop()
