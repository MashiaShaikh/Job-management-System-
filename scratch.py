import tkinter as tk
from tkinter import ttk


class ScrollableTable(tk.Frame):

    def __init__(self, master, rows, headers):
        tk.Frame.__init__(self, master)

        self.canvas = tk.Canvas(self)
        self.table_frame = tk.Frame(self.canvas)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.table_frame, anchor="nw")

        self.table_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.rows = rows
        self.headers = headers
        self.create_table()

    def create_table(self):
        for i, header in enumerate(self.headers):
            label = ttk.Label(self.table_frame, text=header, font=('Helvetica', 11, 'bold'))
            label.grid(row=0, column=i, sticky="nsew")

        for i, row in enumerate(self.rows, start=1):
            for j, cell in enumerate(row):
                label = ttk.Label(self.table_frame, text=cell, font=('Helvetica', 12))
                label.grid(row=i, column=j, sticky="nsew")

        self.table_frame.grid_columnconfigure(0, weight=5, pad=4)
        self.table_frame.grid_rowconfigure(len(self.rows) + 3, weight=1)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)


def main():
    root = tk.Tk()
    root.title("Companies")
    root.geometry("800x400")

    headers = ["Sr. No.", "Company Name", "Job Title", "Job Description", "Experience Required",
               "Salary", "Working Hours", "Apply"]
    rows = [
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
        ["9", "TechGenius Solutions", "IT Support Specialist", "Provides technical assistance and support", "1-3 years",
         "₹4,000,000 - ₹5,000,000", "40 hours/week"],
        ["10", "CloudNine Tech", "DevOps Engineer", "Implements and manages automated deployment pipelines",
         "4-8 years", "₹6,800,000 - ₹9,000,000", "40 hours/week"]

    ]

    scrollable_table = ScrollableTable(root, rows, headers)
    scrollable_table.pack(fill="both", expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
