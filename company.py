from tkinter import *
import tkinter as tk
from customtkinter import *
from tkinter import ttk

from PIL import ImageTk as image

app = tk.Tk()


def sidebar():
    def sign_in():
        app.destroy()
        import E_login

    def home():
        app.destroy()
        import Employee_Portal

    def delete():
        frame.destroy()

    frame = CTkFrame(app, fg_color="white", width=150, height=750)
    frame.place(x=0, y=0)

    applyButton = CTkButton(frame, text="x", text_color="white", fg_color="royal blue1", height=10, width=10,
                            font=("Times New Roman", 30), hover_color="blue", command=delete)
    applyButton.place(x=10, y=10)

    homeButton = CTkButton(frame, text="Home", text_color="royal blue1", fg_color="white", height=10, width=10,
                           font=("Times New Roman", 25), hover_color="blue", command=home)
    homeButton.place(x=10, y=80)

    contactButton = CTkButton(frame, text="Contact Us", text_color="royal blue1", fg_color="white", height=10, width=10,
                              font=("Times New Roman", 25), hover_color="blue")
    contactButton.place(x=10, y=120)

    logoutButton = CTkButton(frame, text="Log Out", text_color="royal blue1", fg_color="white", height=10, width=10,
                             font=("Times New Roman", 28), hover_color="blue", command=sign_in)
    logoutButton.place(x=10, y=600)


# ---background---
app.geometry("1200x650")
app.title("Candidate Portal")
bgImage = image.PhotoImage(file="bg.jpg")
bgLabel = Label(app, image=bgImage)
bgLabel.pack()

applyButton = CTkButton(app, text="☰", text_color="royal blue1", fg_color="white", height=10, width=10,
                        font=("Times New Roman", 30), hover_color="blue", command=sidebar)
applyButton.place(x=10, y=10)


class Table(tk.Frame):
    def __init__(self, parent, rows=10, columns=3):
        super().__init__(parent)

        self.rows = rows
        self.columns = columns
        self.widgets = []

        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = tk.Label(self, text=f'Row {row}\nColumn {column}', borderwidth=0, width=15, height=2)
                label.grid(row=row, column=column, sticky="nsew")
                current_row.append(label)
            self.widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

        self.pack(expand=True)


if __name__ == "__main__":

    table = Table(app, rows=5, columns=3)
    table.pack(expand=True, fill="both")

app.mainloop()
