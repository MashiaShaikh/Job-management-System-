import tkinter as tk


# Function to display profile information
def display_profile():
    # Profile information
    profile_data = {
        "Name": "Mashia Shaikh",
        "Email": "mashiamsshaikh@gmail.com",
        "Phone Number": "+91 7666710927",
        "Address": "Universal College of Engineering, Kaman, Vasai East, Palghar-401202"
    }

    # Create a frame to center the profile information
    frame = tk.Frame(root)
    frame.pack(pady=20)

    # Display profile information in labels
    for i, (key, value) in enumerate(profile_data.items()):
        tk.Label(frame, text=f"{key}: {value}", font=("Helvetica", 12)).grid(row=i, column=0, sticky="w", padx=20,
                                                                             pady=5)


# Create main window
root = tk.Tk()
root.title("Profile Page")

# Set window size
root.geometry("800x400")

# Call function to display profile information
display_profile()

root.mainloop()
