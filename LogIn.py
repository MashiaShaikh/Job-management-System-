from tkinter import *
from tkinter import PhotoImage
from customtkinter import *
from PIL import ImageTk as image
from tkinter import  messagebox
import pymysql

# ---functionality---

def login_user():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error","All Fields Are Required")

    else:
        try:
            con = pymysql.connect(host="localhost",user="root",password="Root")
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
            import candidate_portal


def forgot_pass():
    def change_pass():
        if userEntry == "" or newpassEntry == "" or confirmpassEntry == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=window)
        elif newpassEntry.get() != confirmpassEntry.get():
            messagebox.showerror("Error", "Passwords Mismatch", parent=window)
        else:
            con = pymysql.connect(host="localhost", user="root", password="Root", database="userdata")
            mycursor = con.cursor()
            query = "select * from data where username = %s"
            mycursor.execute(query, (userEntry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Incorrect Username", parent=window)
            else:
                query = "update data set password = %s where username = %s"
                mycursor.execute(query, (newpassEntry.get(), userEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Password is Successfully Reset, Please Log In with New Password",
                                     parent=window)
                window.destroy()

    window = Toplevel()
    window.title("Change Password")

    bgPic = image.PhotoImage(file="changepass.jpg")
    bgLabel = Label(window, image=bgPic)
    bgLabel.grid()

    heading1 = Label(window, text="RESET PASSWORD", bg="white", fg="magenta2",
                    font=("Times New Roman", 19, "bold"))
    heading1.place(x=490, y=60)

    userLabel = Label(window, text="Username", font=("Arial", 10, "bold"),
                          bg="white", fg="magenta2")
    userLabel.place(x=480, y=130)
    userEntry = Entry(window, width=33, font=("Arial", 10, "bold"),
                          bg="orchid1", fg="white")
    userEntry.place(x=490, y=155)

    newpassLabel = Label(window, text="New Password", font=("Arial", 10, "bold"),
                      bg="white", fg="magenta2")
    newpassLabel.place(x=480, y=180)
    newpassEntry = Entry(window, width=33, font=("Arial", 10, "bold"),
                      bg="orchid1", fg="white")
    newpassEntry.place(x=490, y=205)

    confirmpassLabel = Label(window, text="Confirm Password", font=("Arial", 10, "bold"),
                      bg="white", fg="magenta2")
    confirmpassLabel.place(x=480, y=230)
    confirmpassEntry = Entry(window, width=33, font=("Arial", 10, "bold"),
                      bg="orchid1", fg="white")
    confirmpassEntry.place(x=490, y=255)

    lgButton = Button(window, text="SUBMIT", cursor="hand2", width=22, bg="magenta2", fg="white",
                         font=("Microsoft Yauheni UI Light", 12, "bold"), command=change_pass)
    lgButton.place(x=490, y=320)

    window.mainloop()


def signup_page():
    login_window.destroy()
    import SignUp

def show_hide():
    if show_hide_button["text"] == "Show":
        passwordEntry.config(show="")
        show_hide_button.config(text="Hide")

    else:
        passwordEntry.config(show="*")
        show_hide_button.config(text="Show")

login_window = CTk()

# ---background---
login_window.geometry("626x626")
login_window.resizable(0, 0)
login_window.title("Log In Page")
bgImage = image.PhotoImage(file="lg.jpg")
bgLabel = Label(login_window, image=bgImage)
bgLabel.grid()

# ---heading---
heading = Label(login_window, text="CANDIDATE LOGIN", bg="white", fg="deep pink", font=("Times New Roman", 19, "bold"))
heading.place(x=305, y=170)

# ---username---
usernameLabel = Label(login_window, text="Username", font=("Arial", 10, "bold"),
                   bg="white", fg="deep pink")
usernameLabel.place(x=310, y=210)
usernameEntry = Entry(login_window, width=33, font=("Arial", 10, "bold"),
                   bg="deep pink", fg="white")
usernameEntry.place(x=310, y=230)

# ---password---
passwordLabel = Label(login_window, text="Password", font=("Arial", 10, "bold"),
                   bg="white", fg="deep pink")
passwordLabel.place(x=310, y=250)
passwordEntry = Entry(login_window, width=33, font=("Arial", 10, "bold"),
                   bg="deep pink", fg="white", show="*")
passwordEntry.place(x=310, y=270)

show_hide_button = Button(login_window, text="Show",font=("Arial", 7, "bold"), bg="deep pink",
                          fg="white", bd=0, cursor="hand2", command=show_hide)
show_hide_button.place(x=510, y=273)


# ---forget Password---
forgetButton = Button(login_window, text="Forgot Password?", activebackground="white", bd=0, cursor="hand2",
                      font=("Arial", 8), command=forgot_pass)
forgetButton.place(x=445, y=300)

# ---login button---
loginButton = Button(login_window, text="LOG IN", cursor="hand2", width=22, bg="deep pink", fg="white",
                     font=("Microsoft Yauheni UI Light", 12, "bold"), command=login_user)
loginButton.place(x=310, y=345)

signupLabel = Label(login_window, text="Don't Have An Account ?", font=("Microsoft Yauheni UI Light", 8), bg="white")
signupLabel.place(x=345, y=400)

signupButton = Button(login_window, text="SIGN UP", cursor="hand2", font=("Microsoft Yauheni UI Light", 9, "bold"),
                      command=signup_page)
signupButton.place(x=485, y=395)

google_logo = image.PhotoImage(file="google.jpg")
gLabel = Label(login_window, image=google_logo, bg="white")
gLabel.place(x=400, y=425)

login_window.mainloop()
