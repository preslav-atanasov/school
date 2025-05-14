import random
import tkinter as tk
from tkinter import messagebox

qa_dict = {}

def add_flashcard():
    question = question_entry.get()
    category = category_entry.get()
    answer = answer_entry.get()
    if question and category and answer:
        if len(category) < 20:
            questions_listbox.insert(tk.END, f"{question}   |   {category}")
            question_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
            answer_entry.delete(0, tk.END)
            qa_dict[question] = answer
        else:
            messagebox.showwarning("Грешка", "Моля, въведете категория под 20 символа!")
    else:
        messagebox.showwarning("Грешка", "Моля, въведете въпрос, категория и отговор!")

def delete_flashcard():
    question = question_entry.get()
    selected = questions_listbox.curselection()
    if selected:
        questions_listbox.delete(selected)
        qa_dict.pop(question)
    else:
        messagebox.showwarning("Грешка", "Моля, изберете въпрос за изтриване!")

def add_more_flashcards():
    # Hide the elements related to "Test Yourself"
    question_label.pack(side="top", expand=True)
    question_label.config(text="Enter Question:")
    question_entry.pack(side="top", expand=True)
    answer_label.pack(side="top", expand=True)
    answer_entry.pack(side="top", expand=True)
    category_label.pack(side="top", expand=True)
    category_entry.pack(side="top", expand=True)
    add_button.pack(side="top", expand=True)
    delete_button.pack(side="top", expand=True)
    questions_listbox.pack(fill="x", padx=20, side="top", expand=True)
    test_button.pack(side="bottom", expand=True)

    # Update the button text and command
    test_button.config(text="Test Yourself", command=test_yourself)

def test_yourself():
    # Hide the flashcard creation widgets
    question_label.config(text=random.choice(list(qa_dict.keys())))
    question_entry.pack_forget()
    answer_label.pack_forget()
    category_label.pack_forget()
    category_entry.pack_forget()
    add_button.pack_forget()
    delete_button.pack_forget()
    questions_listbox.pack_forget()

    # Display a random question from the dictionary
    random_question = random.choice(list(qa_dict.keys()))
    question_label.config(text=random_question)

    # Update the button text to allow returning to flashcard creation mode
    test_button.config(text="Add more flashcards", command=add_more_flashcards)

root = tk.Tk()
root.geometry("500x500")
root.title("Телефонен указател")

# Flashcard creation widgets
category_label = tk.Label(root, text="Category:")
category_label.pack(side="top", expand=True)
category_entry = tk.Entry(root)
category_entry.pack(side="top", expand=True)

question_label = tk.Label(root, text="Enter Question:")
question_label.pack(side="top", expand=True)
question_entry = tk.Entry(root)
question_entry.pack(fill="x", padx=20, side="top", expand=True)

answer_label = tk.Label(root, text="Enter Answer:")
answer_label.pack(side="top", expand=True)
answer_entry = tk.Entry(root)
answer_entry.pack(fill="x", padx=20, side="top", expand=True)

add_button = tk.Button(root, text="Add Flashcard", command=add_flashcard)
add_button.pack(side="top", expand=True)

questions_listbox = tk.Listbox(root, width=40)
questions_listbox.pack(fill="x", padx=20, side="top", expand=True)

delete_button = tk.Button(root, text="Remove Flashcard", command=delete_flashcard)
delete_button.pack(side="top", expand=True)

# Test mode button
test_button = tk.Button(root, text="Test Yourself", command=test_yourself)
test_button.pack(side="top", expand=True)

root.mainloop()
