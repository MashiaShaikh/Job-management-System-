import tkinter as tk
from tkinter import ttk
from customtkinter import *
import pymysql
from PIL import ImageTk
from PIL import Image

class JobPortalApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("Job Listings")
        self.geometry("1000x450")

        data = [
            ["1", "TechCorp", "Software Engineer", "Develops and maintains software applications", "2-5 years",
             "₹6,000,000 - ₹7,500,000", "40 hours/week"],
            ["2", "DataTech Inc.", "Data Scientist", "Analyzes complex data sets to provide insights", "3-7 years",
             "₹7,500,000 - ₹9,600,000", "40 hours/week"],
            ["3", "Cloud Systems", "Cloud Engineer", "Designs, implements, and manages cloud solutions", "4-8 years",
             "₹6,400,000 - ₹8,200,000", "40 hours/week"],
            ["4", "CyberSec Co.", "Cybersecurity Analyst", "Monitors and responds to security incidents", "2-6 years",
             "₹5,700,000 - ₹7,200,000", "40 hours/week"],
            ["5", "WebWorks Ltd.", "Web Developer", "Designs and builds websites and web applications", "1-4 years",
             "₹5,200,000 - ₹6,700,000", "40 hours/week"],
            ["6", "AI Innovations", "AI Engineer", "Develops and deploys machine learning algorithms", "5-10 years",
             "₹8,000,000 - ₹10,800,000", "40 hours/week"],
            ["7", "Network Sol.", "Network Engineer", "Designs and maintains computer networks", "3-7 years",
             "₹6,400,000 - ₹8,400,000", "40 hours/week"],
            ["8", "MobileTech Co.", "Mobile App Developer", "Develops mobile applications", "2-5 years",
             "₹5,700,000 - ₹7,200,000", "40 hours/week"],
            ["9", "TechGenius Solutions", "IT Support Specialist", "Provides technical assistance and support",
             "1-3 years",
             "₹4,000,000 - ₹5,000,000", "40 hours/week"],
            ["10", "CloudNine Tech", "DevOps Engineer", "Implements and manages automated deployment pipelines",
             "4-8 years", "₹6,800,000 - ₹9,000,000", "40 hours/week"]
        ]

        table = ScrollableTable(self, data)
        table.pack(fill="both", expand=True)


class RegistrationForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Apply for Job")
        self.geometry("500x200")  # Increased width

        tk.Label(self, text="Name:", width=10, font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5,
                                                                            sticky="w")  # Increased width and font size
        self.name_entry = tk.Entry(self, width=30, font=("Helvetica", 12))  # Increased width and font size
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

        tk.Label(self, text="Email:", width=10, font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5,
                                                                             sticky="w")  # Increased width and font size
        self.email_entry = tk.Entry(self, width=30, font=("Helvetica", 12))  # Increased width and font size
        self.email_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

        tk.Label(self, text="Phone:", width=10, font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5,
                                                                             sticky="w")  # Increased width and font size
        self.phone_entry = tk.Entry(self, width=30, font=("Helvetica", 12))  # Increased width and font size
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

        tk.Label(self, text="Experience:", width=10, font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=5,
                                                                                 sticky="w")  # Increased width and font size
        self.job_entry = tk.Entry(self, width=30, font=("Helvetica", 12))  # Increased width and font size
        self.job_entry.grid(row=3, column=1, padx=10, pady=5, sticky="we")

        submit_button = tk.Button(self, text="Submit", command=self.submit_form,
                                  font=("Helvetica", 12))  # Increased font size
        submit_button.grid(row=4, column=0, columnspan=6, pady=10)

    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        job = self.job_entry.get()

        print("Registration Details:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Job Title: {job}")

        # Insert into the database
        self.insert_into_database(name, email, phone, job)

    def insert_into_database(self, name, email, phone, job):
        # Connect to MySQL database
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Root',
                                     database='userdata',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # SQL query to insert registration details
                sql = "INSERT INTO job(name, email, phone, job) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (name, email, phone, job))

            # Commit changes to the database
            connection.commit()
            print("Registration successful")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            # Close the database connection
            connection.close()


class ScrollableTable(tk.Frame):
    def __init__(self, master, data):
        super().__init__(master)

        self.table_frame = tk.Frame(self)

        self.table_frame.pack(fill="both", expand=True)

        self.data = data
        self.create_table()

    def create_table(self):
        headers = ["Serial Number", "Company", "Job Name", "Job Description", "Experience", "Salary", "Working Hours",
                   ""]
        for i, header in enumerate(headers):
            label = ttk.Label(self.table_frame, text=header, font=('Helvetica', 12, 'bold'))
            label.grid(row=0, column=i, sticky="nsew", padx=10, pady=5)

        for i, (serial, company, job_name, job_description, experience, salary, hours) in enumerate(self.data, start=1):
            serial_label = ttk.Label(self.table_frame, text=serial, font=('Helvetica', 10))
            company_label = ttk.Label(self.table_frame, text=company, font=('Helvetica', 10))
            job_name_label = ttk.Label(self.table_frame, text=job_name, font=('Helvetica', 10))
            job_description_label = ttk.Label(self.table_frame, text=job_description, font=('Helvetica', 10))
            experience_label = ttk.Label(self.table_frame, text=experience, font=('Helvetica', 10))
            salary_label = ttk.Label(self.table_frame, text=salary, font=('Helvetica', 10))
            hours_label = ttk.Label(self.table_frame, text=hours, font=('Helvetica', 10))

            apply_button = ttk.Button(self.table_frame, text="Apply", command=lambda idx=i: self.apply_for_job(idx))

            serial_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=5)
            company_label.grid(row=i, column=1, sticky="nsew", padx=10, pady=5)
            job_name_label.grid(row=i, column=2, sticky="nsew", padx=10, pady=5)
            job_description_label.grid(row=i, column=3, sticky="nsew", padx=10, pady=5)
            experience_label.grid(row=i, column=4, sticky="nsew", padx=10, pady=5)
            salary_label.grid(row=i, column=5, sticky="nsew", padx=10, pady=5)
            hours_label.grid(row=i, column=6, sticky="nsew", padx=10, pady=5)
            apply_button.grid(row=i, column=7, sticky="nsew", padx=10, pady=5)

        for i in range(8):
            self.table_frame.grid_columnconfigure(i, weight=1)

    def apply_for_job(self, idx):
        RegistrationForm(self.master)


if __name__ == "__main__":
    app = JobPortalApp()
    app.mainloop()
