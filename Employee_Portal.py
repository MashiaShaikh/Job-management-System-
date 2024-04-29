from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pymysql
import os

app = Tk()


# Function to create a styled sidebar
def create_sidebar():
    def sign_in():
        app.destroy()
        import E_login

    def home():
        app.destroy()
        import Employee_Portal

    def contact():
        os.system("python contact.py")

    def progress():
        import Progress

    def delete():
        frame.destroy()

    frame = Frame(app, bg="royal blue1", width=180, height=650)
    frame.place(x=0, y=0)

    title_label = Label(frame, text="Menu", bg="royal blue1", fg="white", font=("Times New Roman", 20, "bold"))
    title_label.place(x=50, y=10)

    homeButton = Button(frame, text="Home", fg="white", bg="royal blue3", height=2, width=12,
                        font=("Times New Roman", 14, "bold"), command=home)
    homeButton.place(x=20, y=60)

    contactButton = Button(frame, text="Contact Us", fg="white", bg="royal blue3", height=2, width=12,
                           font=("Times New Roman", 14, "bold"),command=contact)
    contactButton.place(x=20, y=120)

    progressButton = Button(frame, text="Progress", fg="white", bg="royal blue3", height=2, width=12,
                            font=("Times New Roman", 14, "bold"), command=progress)
    progressButton.place(x=20, y=180)

    logoutButton = Button(frame, text="Log Out", fg="white", bg="royal blue3", height=2, width=12,
                          font=("Times New Roman", 14, "bold"), command=sign_in)
    logoutButton.place(x=20, y=240)


# ---background---
app.geometry("1200x650")
app.resizable(0, 0)
app.title("Employer Portal")
# bg_image = Image.open("bg.jpg")
# bg_image = bg_image.resize((1200, 650))
# bg_photo = ImageTk.PhotoImage(bg_image)
# bg_label = Label(app, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

create_sidebar()


# Function to display job data in a table
def display_job_data():
    # Connect to MySQL database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Root',
                                 database='userdata',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL query to fetch data from the 'job' table
            sql = "SELECT name, email, phone, job FROM job"
            cursor.execute(sql)
            job_data = cursor.fetchall()

            # Create a styled Treeview widget
            style = ttk.Style()
            style.configure("Treeview", font=("Helvetica", 12))  # Change font size
            style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))  # Change heading font size

            tree = ttk.Treeview(app, columns=("Name", "Email", "Phone", "Job Description"), show="headings", height=20,
                                style="Treeview")
            tree.heading("Name", text="Name")
            tree.heading("Email", text="Email")
            tree.heading("Phone", text="Phone Number")
            tree.heading("Job Description", text="Job Experience")

            tree.column("Name", anchor="center")  # Center align Name column
            tree.column("Email", anchor="center")  # Center align Email column
            tree.column("Phone", anchor="center")  # Center align Phone column
            tree.column("Job Description", anchor="center")  # Center align Job Description column

            tree.place(x=300, y=100)

            # Insert data into the Treeview
            for i, job in enumerate(job_data):
                tree.insert("", "end", values=(job['name'], job['email'], job['phone'], job['job']))
                if i % 2 == 0:
                    tree.tag_configure('evenrow', background='#f0f0f0')
                else:
                    tree.tag_configure('oddrow', background='white')
                tree.tag_configure("oddrow", background="#FFFFFF")
                tree.tag_configure("evenrow", background="#f0f0f0")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the database connection
        connection.close()


# Call the function to display job data
display_job_data()

app.mainloop()
