from tkinter import *
from tkinter import messagebox
import random
from random import randint
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    capital_letters = [chr(i) for i in range(65, 91)]
    lowercase_letters = [chr(i) for i in range(97, 123)]
    number_list = [str(i) for i in range(1, 10)]
    symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*']
    password = []
    for letter in range(randint(5,8)):
        password.append(random.choice(capital_letters))
    for letter in range(3):
        password.append(random.choice(lowercase_letters))
    for number in range(3):
        password.append(random.choice(number_list))
    for symbool in range(3):
        password.append(random.choice(symbol_list))
    random.shuffle(password)
    new_pass = ''.join(password)

    if pass_gen:
        entry_pass.delete(0,END)
        entry_pass.insert(0, new_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_pass.get()
    new_data = {
        website: {
        "email": email,
        "password": password
    }
    }

    if not website  or not password: # if len(website) == 0
        messagebox.showinfo(message="Please make sure haven't left any field empty")
    else:
        try:
            with open("data.jason",mode="r") as data_file:
                #read old data
                data = json.load(data_file)
        except json.decoder.JSONDecodeError:
            with open("data.jason", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)

            with open("data.jason", "w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
                entry_web.delete(0,END)
                entry_pass.delete(0,END)
def search_web():
    website = entry_web.get()
    try:
        with open("data.jason", "r") as data_file:
            data = json.load(data_file)
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error",message= "No data file found")
    else:
        if website in data:
            e = data[website]["email"]
            p = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {e}\nPassword : {p}")
        else:
            messagebox.showinfo(title="Error",message=f"No data file found about {website}")
    finally:
                entry_web.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

#label
website_lebel = Label(text="Website :")
website_lebel.grid(column=0,row=1)

email_label = Label(text="Email/Username :")
email_label.grid(column=0, row=2)

password_label = Label(text="Password :")
password_label.grid(column=0,row=3)

#entry
entry_web = Entry(width=34)
entry_web.grid(row=1,column=1)
entry_web.focus()
entry_email = Entry(width=52)
entry_email.grid(column=1,row=2,columnspan=2)
entry_email.insert(0,"robiul161571@gmail.com")
entry_pass = Entry(width=34)
entry_pass.grid(column=1,row=3)

#button
pass_gen = Button(text="Generate Password",width=14,command=gen_pass)
pass_gen.grid(column=2,row=3)

add = Button(text="Add",width=44,command=save)
add.grid(column=1,row=4,columnspan=2)

search = Button(text="Search",width=14,command=search_web)
search.grid(column=2,row=1)

window.mainloop()


