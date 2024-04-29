from tkinter import *
from PIL import ImageTk, Image


def create_contact_page():
    def close_contact_page():
        contact_page.destroy()

    # Create a new window for the contact page
    contact_page = Tk()
    contact_page.title("Contact Us")
    contact_page.geometry("800x400")

    # Load background image
    bg_image = Image.open("bg.jpg")
    bg_image = bg_image.resize((800, 400))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(contact_page, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Labels for company information with transparent background
    company_email_label = Label(contact_page, text="Company Email:", font=("Helvetica", 16), bg="white", fg="black")
    company_email_label.place(x=400, y=100, anchor="center")

    helpline_number_label = Label(contact_page, text="Helpline Number:", font=("Helvetica", 16), bg="white", fg="black")
    helpline_number_label.place(x=400, y=150, anchor="center")

    location_label = Label(contact_page, text="Location:", font=("Helvetica", 16), bg="white", fg="black")
    location_label.place(x=400, y=200, anchor="center")

    # Company information with transparent background
    company_email_value = Label(contact_page, text="talentforge@gmail.com", font=("Helvetica", 16), bg="white",
                                fg="black")
    company_email_value.place(x=400, y=125, anchor="center")

    helpline_number_value = Label(contact_page, text="+91 1234567890", font=("Helvetica", 14), bg="white", fg="black")
    helpline_number_value.place(x=400, y=175, anchor="center")

    location_value = Label(contact_page, text="Universal College Of Engineering, Kaman Road", font=("Helvetica", 16),
                           bg="white", fg="black")
    location_value.place(x=400, y=225, anchor="center")

    # Button to close the contact page
    close_button = Button(contact_page, text="Close", command=close_contact_page)
    close_button.place(x=400, y=300, anchor="center")

    # Run the contact page
    contact_page.mainloop()


# Create the contact page
create_contact_page()
