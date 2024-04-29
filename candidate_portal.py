from tkinter import *
from customtkinter import *
import apply
from PIL import ImageTk
from PIL import Image
import customtkinter
import os

app = CTk()

def open():
    os.system("python contact.py")


def hired():
    apply.JobPortalApp().mainloop()


def view_profile():
    import profile


def sidebar():
    def sign_in():
        app.destroy()
        import LogIn

    def home():
        app.destroy()
        import candidate_portal

    def delete():
        frame.destroy()

    frame = CTkFrame(app, fg_color="white", width=150, height=448)
    frame.place(x=0, y=0)

    applyButton = CTkButton(frame, text="x", text_color="white", fg_color="royal blue1", height=10, width=10,
                            font=("Times New Roman", 30), hover_color="blue", command=delete)
    applyButton.place(x=10, y=10)

    homeButton = CTkButton(frame, text="Home", text_color="royal blue1", fg_color="white", height=10, width=10,
                           font=("Times New Roman", 25), hover_color="blue", command=home)
    homeButton.place(x=10, y=80)

    contactButton = CTkButton(frame, text="Contact Us", text_color="royal blue1", fg_color="white", height=10, width=10,
                              font=("Times New Roman", 25), hover_color="blue",command=open)
    contactButton.place(x=10, y=120)

    logoutButton = CTkButton(frame, text="Log Out", text_color="royal blue1", fg_color="white", height=10, width=10,
                             font=("Times New Roman", 28), hover_color="blue", command=sign_in)
    logoutButton.place(x=10, y=400)


# ---background---
app.geometry("848x448")
app.resizable(0, 0)
app.title("Candidate Portal")
# bg_image = Image.open("background.png")
# bg_image = bg_image.resize((1200, 650))
# bg_photo = ImageTk.PhotoImage(bg_image)
# bg_label = Label(app, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

applyButton = CTkButton(app, text="Get Hired", text_color="white", fg_color="royal blue1", height=50, width=200,
                        font=("Times New Roman", 30, "italic"), hover_color="blue", command=hired)
applyButton.place(x=330, y=200)

side_bar = CTkButton(app, text="☰", text_color="royal blue1", fg_color="white", height=10, width=10,
                     font=("Times New Roman", 30), hover_color="blue", command=sidebar)
side_bar.place(x=10, y=10)

# Button to view candidate's profile
profile_button = CTkButton(app, text="Profile", text_color="royal blue1", fg_color="white", height=10, width=10,
                            font=("Times New Roman", 20), hover_color="blue", command=view_profile)
profile_button.place(relx=1.0, x=-10, y=10, anchor=NE)

app.mainloop()
