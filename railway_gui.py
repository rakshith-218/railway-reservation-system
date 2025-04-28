import tkinter as tk
from tkinter import messagebox

# Initial train data
trains = {
    "101": {"name": "Express 1", "seats": 5},
    "102": {"name": "Express 2", "seats": 5}
}

bookings = []

# GUI Functions
def show_trains():
    output = "Train No\tName\t\tAvailable Seats\n"
    for train_no, details in trains.items():
        output += f"{train_no}\t\t{details['name']}\t{details['seats']}\n"
    messagebox.showinfo("Available Trains", output)

def book_ticket():
    name = name_entry.get()
    train_no = train_entry.get()

    if name == "" or train_no == "":
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    if train_no in trains and trains[train_no]["seats"] > 0:
        trains[train_no]["seats"] -= 1
        bookings.append({"name": name, "train_no": train_no})
        messagebox.showinfo("Success", f"Ticket booked for {name} in Train {train_no}")
    else:
        messagebox.showerror("Booking Failed", "Invalid train number or no seats available.")

def view_bookings():
    if not bookings:
        messagebox.showinfo("Bookings", "No bookings yet.")
        return
    output = "Name\t\tTrain No\n"
    for b in bookings:
        output += f"{b['name']}\t\t{b['train_no']}\n"
    messagebox.showinfo("All Bookings", output)

# Tkinter GUI setup
root = tk.Tk()
root.title("Railway Reservation System")

# Labels and Entries
tk.Label(root, text="Passenger Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Train Number:").grid(row=1, column=0, padx=10, pady=5)
train_entry = tk.Entry(root)
train_entry.grid(row=1, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Show Trains", command=show_trains).grid(row=2, column=0, pady=10)
tk.Button(root, text="Book Ticket", command=book_ticket).grid(row=2, column=1, pady=10)
tk.Button(root, text="View Bookings", command=view_bookings).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
