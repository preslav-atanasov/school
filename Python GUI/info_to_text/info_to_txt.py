from tkinter import *
from tkinter import messagebox


def save_to_file():
    # Gather data from the form
    first_name = name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    request = request_entry.get("1.0", END).strip()  # Get text from Text widget and remove trailing newline
    gender = gender_var.get()
    education = education_var.get()

    # Prepare data for saving
    if not first_name or not last_name or not email or not gender or not education:
        print("Error: All fields are required!")
        messagebox.showwarning("Error", "All fields are required!")
        return

    data = (
        f"First Name: {first_name}\n"
        f"Last Name: {last_name}\n"
        f"Email: {email}\n"
        f"Request: {request}\n"
        f"Gender: {gender}\n"
        f"Education: {education}\n"
        "------------------------\n"
    )

    # Save data to a file
    with open("form_data.txt", "a") as file:
        file.write(data)

    # Confirm success
    print("Data saved successfully!")


root = Tk()
root.title("Save to file")

# Name
name_label = Label(root, text="First name:")
name_entry = Entry(root)
name_label.grid(row=0, column=1, padx=10, pady=10, sticky=W)
name_entry.grid(row=0, column=2, padx=10, pady=10, sticky=W)

# Last Name
last_name_label = Label(root, text="Last name:")
last_name_entry = Entry(root)
last_name_label.grid(row=1, column=1, padx=10, pady=10, sticky=W)
last_name_entry.grid(row=1, column=2, padx=10, pady=10, sticky=W)

# Email
email_label = Label(root, text="Email:")
email_entry = Entry(root)
email_label.grid(row=2, column=1, padx=10, pady=10, sticky=W)
email_entry.grid(row=2, column=2, padx=10, pady=10, sticky=W)

# Request
text_label = Label(root, text="Request:")
request_entry = Text(root, width=20, height=5)
text_label.grid(row=3, column=1, padx=10, pady=10, sticky=W)
request_entry.grid(row=3, column=2, padx=10, pady=10, sticky=W)

# Gender
gender_label = Label(root, text="Gender:")
gender_entry = Frame(root)
gender_label.grid(row=4, column=1, padx=10, pady=10, sticky=W)
gender_entry.grid(row=4, column=2, padx=10, pady=10, sticky=W)

gender_var = StringVar(value="0")
radio_male = Radiobutton(gender_entry, text="Male", variable=gender_var, value="Male")
radio_female = Radiobutton(gender_entry, text="Female", variable=gender_var, value="Female")

radio_male.grid(row=0, column=0, padx=10, pady=5, sticky=W)
radio_female.grid(row=0, column=1, padx=10, pady=5, sticky=W)

# Education
education_label = Label(root, text="Education:")
education_entry = Frame(root)
education_label.grid(row=5, column=1, padx=10, pady=10, sticky=W)
education_entry.grid(row=5, column=2, padx=10, pady=10, sticky=W)

education_var = StringVar(value="0")

radio_highschool = Radiobutton(education_entry, text="Highschool", variable=education_var, value="Highschool")
radio_bachelors = Radiobutton(education_entry, text="Bachelor's", variable=education_var, value="Bachelor's")
radio_masters = Radiobutton(education_entry, text="Master's", variable=education_var, value="Master's")

radio_highschool.grid(row=0, column=0, padx=10, pady=5, sticky=W)
radio_bachelors.grid(row=1, column=0, padx=10, pady=5, sticky=W)
radio_masters.grid(row=2, column=0, padx=10, pady=5, sticky=W)

# Submit
button_submit = Button(root, text="Submit!", command=save_to_file)
button_submit.grid(row=6, columnspan=3, padx=10, pady=10, sticky=EW)

root.mainloop()
