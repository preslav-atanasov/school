from tkinter import *
from PIL import Image, ImageTk

image_count = 1
size = (650, 750)


def previous_image():
    global image_count, photo, label
    if image_count > 1:
        image_count -= 1

    try:
        changed_image = Image.open(f"{image_count}.png")
        resized_changed_image = changed_image.resize(size)
        photo = ImageTk.PhotoImage(resized_changed_image)

        label.config(image=photo)
        label.image = photo
    except FileNotFoundError:
        label.config(image='', text="File not found")


def next_image():
    global image_count, photo, label
    if image_count < 12:
        image_count += 1

    try:
        changed_image = Image.open(f"{image_count}.png")
        resized_changed_image = changed_image.resize(size)
        photo = ImageTk.PhotoImage(resized_changed_image)

        label.config(image=photo)
        label.image = photo
    except FileNotFoundError:
        label.config(image='', text="File not found")


root = Tk()

image = Image.open(f"{image_count}.png")
resized_image = image.resize(size)
photo = ImageTk.PhotoImage(resized_image)

label = Label(root, image=photo)
label.grid(row=0, column=1)

button_prev = Button(root, text="Previous", command=previous_image)
button_next = Button(root, text="Next", command=next_image)
button_prev.grid(row=0, column=0, padx=10, pady=10)
button_next.grid(row=0, column=2, padx=10, pady=10)

root.title("Calendar 2025")
root.mainloop()
