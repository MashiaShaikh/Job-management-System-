from tkinter import *
from tkinter import messagebox
from PIL import ImageTk as image
import pymysql

login_window = Tk()


# ---functionalities---

def connect_database():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "All Fields Are Required !")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="Root")
            mycursor = con.cursor()
        except:
            messagebox.showerror("Error", "Connection is not Established, Try Again !")
            return
        query = "use userdata"
        mycursor.execute(query)
        query = "select * from data where username = %s and password = %s"
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "Invalid Username or Password")
        else:
            messagebox.showinfo("Success", "Log In is Successful")
            import Employee_Portal


def show_hide():
    if show_hide_button["text"] == "Show":
        passwordEntry.config(show="")
        show_hide_button.config(text="Hide")

    else:
        passwordEntry.config(show="*")
        show_hide_button.config(text="Show")


# ---background---
login_window.geometry("610x410")
login_window.resizable(0, 0)
login_window.title("LogIn")
bgImage = image.PhotoImage(file="lg.jpg")
bgLabel = Label(login_window, image=bgImage)
bgLabel.pack()

# ---heading---
heading = Label(login_window, text="EMPLOYER LOGIN", bg="white", fg="deep pink",
                font=("Times New Roman", 19, "bold"))
heading.place(x=295, y=50)

# ---employee id---
usernameLabel = Label(login_window, text="Employee ID", font=("Arial", 10, "bold"),
                      bg="white", fg="deep pink")
usernameLabel.place(x=310, y=100)
usernameEntry = Entry(login_window, width=33, font=("Arial", 10, "bold"),
                      bg="deep pink", fg="white")
usernameEntry.place(x=300, y=120)

# ---password---
passwordLabel = Label(login_window, text="Password", font=("Arial", 10, "bold"),
                      bg="white", fg="deep pink")
passwordLabel.place(x=310, y=150)
passwordEntry = Entry(login_window, width=33, font=("Arial", 10, "bold"),
                      bg="deep pink", fg="white", show="*")
passwordEntry.place(x=300, y=170)

show_hide_button = Button(login_window, text="Show", font=("Arial", 7, "bold"), bg="deep pink",
                          fg="white", bd=0, cursor="hand2", command=show_hide)
show_hide_button.place(x=500, y=174)

# ---login button---
loginButton = Button(login_window, text="LOG IN", cursor="hand2", width=21, bg="deep pink", bd=1, fg="white",
                     font=("Microsoft Yauheni UI Light", 12, "bold"), command=connect_database)
loginButton.place(x=307, y=210)

login_window.mainloop()
