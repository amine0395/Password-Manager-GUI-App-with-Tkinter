from tkinter import  *
import pyperclip
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def rand():

   letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
   symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

   nr_letters = random.randint(8, 10)
   nr_symbols = random.randint(2, 4)
   nr_numbers = random.randint(2, 4)
   password_list = []
   for char in range(1, nr_letters + 1):
      password_list.append(random.choice(letters))
   for char in range(1, nr_symbols + 1):
      password_list += random.choice(symbols)

   for char in range(1, nr_numbers + 1):
      password_list += random.choice(numbers)
   random.shuffle(password_list)
   password = ""
   for char in password_list:
      password += char
   paswrd_entry.delete(0, END)
   paswrd_entry.insert(0, str(password))
   pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
   website = website_entry.get()
   email=email_entry.get()
   passwrd=paswrd_entry.get()

   if len(website) ==0 or len(passwrd) ==0 :
      messagebox.showinfo(title="Field empty",message="please enter all necessary data")
   else:
      ok = messagebox.askyesno(title=website, message="Are you sure these are your info: \n Email: " + str(email) + "\n password: " + str(passwrd))
      if ok:
         with open("data.txt", "a") as data_file:
            data_file.write(str(website) + " | " + str(email) + " | " + str(passwrd) + "\n")
            website_entry.delete(0, END)
            paswrd_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50,pady=50)
window.iconbitmap("logo.ico")


canvas = Canvas(width=200 ,height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website_lbl=Label(text="Website: ")
website_lbl.grid(row=1,column=0)
email_lbl=Label(text="Email/Username: ")
email_lbl.grid(row=2,column=0)
paswrd_lbl=Label(text="Password: ")
paswrd_lbl.grid(row=3,column=0)


website_entry = Entry(width=52)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"@gmail.com")
paswrd_entry = Entry(width=34)
paswrd_entry.grid(row=3,column=1)


paswrd_btn=Button(text="Generate password",command=rand)
paswrd_btn.grid(row=3,column=2)
add_btn=Button(text="Add",width=44,command=save)
add_btn.grid(row=4,column=1,columnspan=2)
window.mainloop()
