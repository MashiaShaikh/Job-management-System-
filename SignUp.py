from tkinter import *
import pymysql
from PIL import ImageTk as image
from tkinter import messagebox

signup_window = Tk()


# ---functionalities---

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmpasswordEntry.delete(0, END)
    check.set(0)


def connect_database():
    if emailEntry.get() == "" or usernameEntry.get() == "" or passwordEntry.get() == "" or confirmpasswordEntry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required !")
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror("Error", "Password Mismatch !")
    elif check.get() == 0:
        messagebox.showerror("Error", "Please Accept The Terms And Conditions !")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="Root")
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", "Database Connectivity Issue, Please Try Again !")
            return
        try:
            query = "create database userdata"
            mycursor.execute(query)
            query = "use userdata"
            mycursor.execute(query)
            query = ("create table data(id int auto_increment primary key not null, email varchar(50), username "
                     "varchar("
                     "100), password varchar(20))")
            mycursor.execute(query)
        except:
            mycursor.execute("use userdata")

        query = "select * from data where username=%s"
        mycursor.execute(query, (usernameEntry.get()))

        row = mycursor.fetchone()
        if row is not None:
            messagebox.showerror("Error", "Username Already Exists")
        else:

            query = "insert into data(email, username, password) values (%s, %s, %s)"
            mycursor.execute(query,
                             (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration is Successful")
            clear()
            signup_window.destroy()
            import LogIn


def login_page():
    signup_window.destroy()
    import LogIn


# ---background---
signup_window.title("Sign Up")
signup_window.resizable(0, 0)
background = image.PhotoImage(file="su.jpg")
bgLabel = Label(signup_window, image=background)
bgLabel.grid()

# ---heading---
heading = Label(signup_window, text="Create An Account", font=("Times New Roman", 23, "bold"),
                bg="white", fg="royal blue1")
heading.place(x=300, y=40)

# ---email---
emailLabel = Label(signup_window, text="E-mail", font=("Arial", 10, "bold"),
                   bg="white", fg="royal blue1")
emailLabel.place(x=320, y=90)
emailEntry = Entry(signup_window, width=35, font=("Arial", 10, "bold"),
                   bg="royal blue1", fg="white")
emailEntry.place(x=310, y=110)

# ---username---
usernameLabel = Label(signup_window, text="Username", font=("Arial", 10, "bold"),
                      bg="white", fg="royal blue1")
usernameLabel.place(x=320, y=135)
usernameEntry = Entry(signup_window, width=35, font=("Arial", 10, "bold"),
                      bg="royal blue1", fg="white")
usernameEntry.place(x=310, y=155)

# ---password---
passwordLabel = Label(signup_window, text="Password", font=("Arial", 10, "bold"),
                      bg="white", fg="royal blue1")
passwordLabel.place(x=320, y=180)
passwordEntry = Entry(signup_window, width=35, font=("Arial", 10, "bold"),
                      bg="royal blue1", fg="white")
passwordEntry.place(x=310, y=200)

# ---confirm password---
confirmpasswordLabel = Label(signup_window, text="Confirm Password", font=("Arial", 10, "bold"),
                             bg="white", fg="royal blue1")
confirmpasswordLabel.place(x=320, y=225)
confirmpasswordEntry = Entry(signup_window, width=35, font=("Arial", 10, "bold"),
                             bg="royal blue1", fg="white")
confirmpasswordEntry.place(x=310, y=245)

# ---checkbutton---
check = IntVar()
termsandconditions = Checkbutton(signup_window, text="I Agree To The Terms And Conditions",
                                 font=("Arial", 10, "bold"), bd=0, bg="white", fg="royal blue1", variable=check)
termsandconditions.place(x=300, y=285)

# ---sign up button---
signupButton = Button(signup_window, text="SIGN UP", cursor="hand2", width=24, bg="royal blue1", fg="white",
                      font=("Microsoft Yauheni UI Light", 12, "bold"), command=connect_database)
signupButton.place(x=310, y=310)

loginLabel = Label(signup_window, text="Already Have An Account ?", font=("Arial", 8), bg="white")
loginLabel.place(x=310, y=350)

loginButton = Button(signup_window, text="LOG IN", cursor="hand2", font=("Microsoft Yauheni UI Light", 10, "bold")
                     , bd=0, bg="white", fg="royal blue1", command=login_page)
loginButton.place(x=455, y=347)

signup_window.mainloop()
