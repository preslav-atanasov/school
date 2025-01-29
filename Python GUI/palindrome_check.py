from tkinter import *


def check_palindrome():
    word = entry.get().strip().replace(" ", "").lower()
    if word == word[::-1]:
        result = f'\"result\" e palindrome!'
    else:
        result = f'\"result\" ne e palindrome!'

    labelresult = Label(root, text=result)
    labelresult.pack()


def myClick2():
    label = Label(root, text="17", fg="#000000")
    label.pack()


root = Tk()
my_label = Label(root, text="Check for palindrome:", fg="#dd00aa")
my_label.pack()

button = Button(root, text="Check", command=check_palindrome)
button.pack()

entry = Entry(root)
entry.pack()

root.mainloop()