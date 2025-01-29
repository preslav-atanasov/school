import tkinter as tk
from tkinter import messagebox


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        if phone.isalnum() and len(phone) == 10:
            contacts_listbox.insert(tk.END, f"{name}: {phone}")
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Грешка", "Моля, въведете валиден телефонен номер!")
    else:
        messagebox.showwarning("Грешка", "Моля, въведете име и телефонен номер!")


def delete_contact():
    selected = contacts_listbox.curselection()
    if selected:
        contacts_listbox.delete(selected)
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

# Бутон за добавяне на контакт
add_button = tk.Button(root, text="Добави контакт", command=add_contact)
add_button.grid(row=5, column=1)

# Списък с контакти
contacts_listbox = tk.Listbox(root, width=40)
contacts_listbox.grid(row=6, column=1, padx=5, pady=5)

# Бутон за изтриване на контакт
delete_button = tk.Button(root, text="Изтрий контакт", command=delete_contact)
delete_button.grid(row=7, column=1, padx=5, pady=5)

# Стартиране на приложението
root.mainloop()
