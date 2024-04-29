from tkinter import *

from PIL import ImageTk as image

welcome_window = Tk()


# ---functionalities---
def login_page():
    welcome_window.destroy()
    import LogIn


def log_page():
    welcome_window.destroy()
    import E_login


# ---background---
welcome_window.geometry("610x410")
welcome_window.resizable(0, 0)
welcome_window.title("Welcome")
bgImage = image.PhotoImage(file="welcome.jpeg")
bgLabel = Label(welcome_window, image=bgImage)
bgLabel.pack()

# ---heading1---
heading1 = Label(welcome_window, text="TalentForge", font=("Times New Roman", 20, "bold"),
                 bg="white", fg="dark slate gray")
heading1.place(x=240, y=5)
heading = Label(welcome_window, text="Find Your Career. You Deserve It.", font=("Times New Roman", 20, "bold"),
                bg="white", fg="dark slate gray")
heading.place(x=100, y=40)

# ---heading2---
heading = Label(welcome_window, text="Are You A ?!", font=("Times New Roman", 16, "bold"),
                bg="white", fg="dark slate gray", bd=0)
heading.place(x=265, y=150)

# ---candidate button---
candidateButton = Button(welcome_window, text="CANDIDATE", cursor="hand2", width=15, bg="dark slate gray", fg="white",
                         font=("Microsoft Yauheni UI Light", 11, "bold"), bd=1, command=login_page)
candidateButton.place(x=145, y=370)

# ---employer button---
employerButton = Button(welcome_window, text="EMPLOYER", cursor="hand2", width=15, bg="dark slate gray", fg="white",
                        font=("Microsoft Yauheni UI Light", 11, "bold"), bd=1, command=log_page)
employerButton.place(x=335, y=370)

welcome_window.mainloop()
