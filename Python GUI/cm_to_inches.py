from tkinter import *


def cm_to_inches():
    try:
        cm = float(cm_entry.get())
        inches = cm / 2.54
        inches_label.config(text=f"Inches: {inches:.2f}", fg="#000000")
    except ValueError:
        inches_label.config(text=f"Please enter a valid input.", fg="#ff0000")


root = Tk()
root.title("Converter")
root.minsize(300, 150)
root.maxsize(300, 150)

cm_label = Label(root, text="Centimeters: ")
cm_label.pack()

cm_entry = Entry(root)
cm_entry.pack()

convert_button = Button(root, text="Convert!", command=cm_to_inches)
convert_button.pack()

inches_label = Label(root, text="Inches: ")
inches_label.pack()

root.mainloop()
