from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from random import randint,choice,shuffle
from pyexpat.errors import messages
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    char =[choice(letters) for char in range(randint(8, 10))]
    sym = [choice(symbols) for sym in range(randint(2, 4))]
    num = [choice(numbers) for num in range(randint(2, 4))]
    password_list = char+sym+num
    shuffle(password_list)

    password = "".join(password_list)
    password_field.delete(0,"end")
    password_field.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = text.get()
    Email = name.get()
    password = password_field.get()
    new_data = {website:{"Email":Email , "Password":password}}
    if len(website)==0  or len(Email) == 0:
        messagebox.showerror(title="OOPS", message="Please don't Leave any fields empty")
    else:
        try:
            with open("save_credentials.json", "r") as file:
                data=json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("save_credentials.json" ,"w") as file1:
                json.dump(new_data,file1,indent=4)
        else:
            with open("save_credentials.json" ,"w") as file2:
                json.dump(data,file2,indent=4)
        finally:
                text.delete(0,"end")
                password_field.delete(0,"end")



def find_password():
    website = text.get()
    try:
        with open("save_credentials.json", "r") as file:
            data = json.load(file)
    except:
        messagebox.showerror(title="OOPS", message="No Data File Found")
    else:
            if website in data:
                email = data[website]["Email"]
                password = data[website]["Password"]
                messagebox.showinfo(title=website,message=f"Email: {email}\n Password: {password}")
            else:
                messagebox.showerror(title="OOPS", message=f"No Details for the {website} Found")





# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website = Label(text="Website:")
website.grid(row=1,column=0)

text=Entry(width=32)
text.focus()
text.grid(row=1,column=1)

search = Button(text="Search",width=13,command=find_password)
search.grid(row=1,column=2)

email = Label(text="Email/Username:")
email.grid(row=2,column=0)

name=Entry(width=51)
name.focus( )
name.insert(0,"vasanthkumar0132@gmail.com")
name.grid(row=2,column=1,columnspan=2)

password = Label(text="Password:")
password.grid(row=3,column=0)

password_field=Entry(width=32)
password_field.focus()
password_field.grid(row=3,column=1)

generate = Button(text="Generate Password",command=password_gen)

generate.grid(row=3,column=2)

add = Button(text="Add",width=45,command=save)
add.grid(row=4,column=1,columnspan=2)






window.mainloop()