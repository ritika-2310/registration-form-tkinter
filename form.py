import tkinter.messagebox as tmsg  # For showing popup messages like errors or success
from tkinter import *  # Import all tkinter widgets
from tkinter import ttk  # For themed widgets like Scrollbar
from PIL import Image, ImageTk  # For loading and resizing background image
#from tabulate import tabulate  # Used to format data tables 
#import sys  # For system-level functions
import mysql.connector  # Main library to connect to MySQL
import mysql  # General MySQL package (optional)

# Connect to MySQL database
mydb = mysql.connector.connect(host="localhost", user="root", passwd="123", database="CDS")  # Connect to CDS database
mycursor = mydb.cursor()  # Cursor to run queries

# Set up the main window
root = Tk()  # Create the main tkinter window
root.geometry('1530x1530')  # Fix size of window
root.minsize(1530, 1530)  # Minimum size constraint
root.maxsize(1530, 1530)  # Maximum size constraint

# Load and display background image
i1 = Image.open('CDSbg.jpg')  # Load image
i1 = i1.resize((1530, 1530), Image.Resampling.LANCZOS)  # Resize image to match window size
Tk.img = ImageTk.PhotoImage(i1)  # Convert image for tkinter display
label = Label(image=Tk.img)  # Create label for image
label.place(x=0, y=0)  # Position it at top-left corner
root.update()  # Force window to update layout
# Function: insertget() - Insert data into database
def insertget(e, e1, e2, e3, e4, e5, e6, e7, e8):
    entry = e.get()  # Get value from entry field
    name = e1.get()
    age = e2.get()
    gender = e3.get()
    mother = e4.get()
    father = e5.get()
    nationality = e6.get()
    minority = e7.get()
    email = e8.get()

    hintlist = [  # Placeholder list
        'Enter your entry number',
        'Enter your name',
        'Enter your age',
        'Enter your gender',
        "Enter your mother's name",
        "Enter your father's name",
        "Are you an Indian?(yes/no)",
        "Do you belong to minority?(yes/no)",
        "Enter your email i'd"
    ]
    inputs = [entry, name, age, gender, mother, father, nationality, minority, email]

    for i in range(len(inputs)):  # Check if any field is empty or still has placeholder
        if inputs[i].strip() == "" or inputs[i] == hintlist[i]:
            tmsg.showerror("Input Error", f"Please fill out all fields.\nMissing or default value: {hintlist[i]}")
            return

    try:
        q = "insert into entries(entryno, name, age, gender, mother, father, nationality, minority, email) values ({}, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}')".format(
            int(entry), name, int(age), gender, mother, father, nationality, minority, email)
        mycursor.execute(q)  # Execute query
        mydb.commit()  # Save changes to DB
        tmsg.showinfo("Message", "Entry recorded successfully!")
    except:
        tmsg.showerror("Error", "Could not insert entry. Check input types or DB connection.")
def clear_placeholder(event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, END)
# Function: insert() - Show GUI form for new entry
def insert():
    frame1 = Frame(root, bg='black', width=1000, height=700)
    frame1.place(relx=0.5, y=20, anchor='n')

    # All entry fields with placeholder + focus clear
    e = Entry(frame1, width=50)
    e.pack()
    e.insert(0, 'Enter your entry number')
    e.bind("<FocusIn>", lambda event: clear_placeholder(event, e, 'Enter your entry number'))

    e1 = Entry(frame1, width=50)
    e1.pack()
    e1.insert(0, 'Enter your name')
    e1.bind("<FocusIn>", lambda event: clear_placeholder(event, e1, 'Enter your name'))

    e2 = Entry(frame1, width=50)
    e2.pack()
    e2.insert(0, 'Enter your age')
    e2.bind("<FocusIn>", lambda event: clear_placeholder(event, e2, 'Enter your age'))

    e3 = Entry(frame1, width=50)
    e3.pack()
    e3.insert(0, 'Enter your gender')
    e3.bind("<FocusIn>", lambda event: clear_placeholder(event, e3, 'Enter your gender'))

    e4 = Entry(frame1, width=50)
    e4.pack()
    e4.insert(0, "Enter your mother's name")
    e4.bind("<FocusIn>", lambda event: clear_placeholder(event, e4, "Enter your mother's name"))

    e5 = Entry(frame1, width=50)
    e5.pack()
    e5.insert(0, "Enter your father's name")
    e5.bind("<FocusIn>", lambda event: clear_placeholder(event, e5, "Enter your father's name"))

    e6 = Entry(frame1, width=50)
    e6.pack()
    e6.insert(0, "Are you an Indian?(yes/no)")
    e6.bind("<FocusIn>", lambda event: clear_placeholder(event, e6, "Are you an Indian?(yes/no)"))

    e7 = Entry(frame1, width=50)
    e7.pack()
    e7.insert(0, "Do you belong to minority?(yes/no)")
    e7.bind("<FocusIn>", lambda event: clear_placeholder(event, e7, "Do you belong to minority?(yes/no)"))

    e8 = Entry(frame1, width=50)
    e8.pack()
    e8.insert(0, "Enter your email i'd")
    e8.bind("<FocusIn>", lambda event: clear_placeholder(event, e8, "Enter your email i'd"))

    Button(frame1, text='Submit',bg="#63edba", command=lambda: [insertget(e, e1, e2, e3, e4, e5, e6, e7, e8), frame1.destroy()]).pack()
# Function: display() - Display all entries from DB
def display():
    frame1 = Frame(root, bg='black', width=1000, height=500)
    frame1.place(relx=0.5, y=20, anchor='n')

    l1 = []
    l = Text(frame1, bg='purple', fg='yellow', font=('Helvetica', 18, 'bold'), width=50, height=10)
    l.insert(END, 'The entries are-:\n\n', "left_margin")
      # Add left inner padding
    mycursor.execute("SELECT * FROM entries")
    l.tag_configure("left_margin", lmargin1=20)
    data = mycursor.fetchall()
    for entry in data:
        l.insert(END, f"Entry No: {entry[0]}\n","left_margin")
        l.insert(END, f"Name: {entry[1]}\n", "left_margin")
        l.insert(END, f"Age: {entry[2]}\n", "left_margin")
        l.insert(END, f"Gender: {entry[3]}\n", "left_margin")
        l.insert(END, f"Mother: {entry[4]}\n", "left_margin")
        l.insert(END, f"Father: {entry[5]}\n", "left_margin")
        l.insert(END, f"Nationality: {entry[6]}\n", "left_margin")
        l.insert(END, f"Minority: {entry[7]}\n", "left_margin")
        l.insert(END, f"Email: {entry[8]}\n", "left_margin")
        l.insert(END, "-----------------------------\n\n", "left_margin")
    l.pack(anchor='nw')
    #scrollbar = ttk.Scrollbar(frame1, orient=VERTICAL, command=l.yview)
    #scrollbar.pack(side=RIGHT, fill=Y)
    #l.configure(yscrollcommand=scrollbar.set)
    style = ttk.Style()
    style.configure("Vertical.TScrollbar", background="#af4063", arrowcolor="white")
    scrollbar = ttk.Scrollbar(frame1, orient=VERTICAL, command=l.yview, style="Vertical.TScrollbar")
    Button(frame1, text='Exit', font=('Helvetica', 18, 'bold'), width=20,padx=15, bg="#32639e",fg="#c8f0b1", command=frame1.destroy).pack(anchor='center')
    # Function: search() and searchget() - Search a specific entry
def searchget(e):
    frame1 = Frame(root, bg='black', width=1000, height=500)
    frame1.place(relx=0.5, y=100, anchor='n')  # Optional y=100 to avoid overlap
    try:
        n = int(e.get())
    except ValueError:
        tmsg.showerror("Error", "Please enter a valid number.")
        return
    l = Text(frame1, bg='purple', fg='yellow', font=('Helvetica', 18, 'bold'), width=50, height=10)
    l.insert(END, 'The searched entry is-:\n')
    mycursor.execute("SELECT * FROM entries WHERE entryno=%s", (n,))
    data = mycursor.fetchall()
    if data == []:
        tmsg.showinfo("Error", "Entry not found!")
    else:
        for entry in data:
            l.insert(END, f"Entry No: {entry[0]}\n")
            l.insert(END, f"Name: {entry[1]}\n")
            l.insert(END, f"Age: {entry[2]}\n")
            l.insert(END, f"Gender: {entry[3]}\n")
            l.insert(END, f"Mother: {entry[4]}\n")
            l.insert(END, f"Father: {entry[5]}\n")
            l.insert(END, f"Nationality: {entry[6]}\n")
            l.insert(END, f"Minority: {entry[7]}\n")
            l.insert(END, f"Email: {entry[8]}\n")
            l.insert(END, "-----------------------------\n\n")
        l.pack(fill=BOTH)
        Button(frame1, text='Exit', font=('Helvetica', 18, 'bold'), width=20, bg="#32639e", fg="#c8f0b1",padx=15, command=frame1.destroy).pack(anchor='center')
def search():
    frame1 = Frame(root, bg='black', width=1000, height=500)
    frame1.place(relx=0.5, y=20, anchor='n')  # Top-center at y=20

    e = Entry(frame1, width=50)
    e.pack()
    e.insert(0, 'Enter your entry number')
    e.bind("<FocusIn>", lambda event: clear_placeholder(event, e, f'Enter your entry number'))
    Button(frame1, text='Submit',padx=15 ,bg="#af4063",fg="#c8f0b1",command=lambda: [searchget(e), frame1.destroy()]).pack()
# Update entry - each field update function
def n(e, e1): mycursor.execute("UPDATE entries SET name=%s WHERE entryno=%s", (e1, e)); mydb.commit(); tmsg.showinfo("Message", "Entry updated successfully!")
def n1(e, e1): mycursor.execute("UPDATE entries SET age=%s WHERE entryno=%s", (e1, e)); mydb.commit(); tmsg.showinfo("Message", "Entry updated successfully!")
def n2(e, e1): mycursor.execute("UPDATE entries SET gender=%s WHERE entryno=%s", (e1, e)); mydb.commit(); tmsg.showinfo("Message", "Entry updated successfully!")
def n3(e, e1): mycursor.execute("UPDATE entries SET mother=%s WHERE entryno=%s", (e1, e)); mydb.commit(); tmsg.showinfo("Message", "Entry updated successfully!")
def n4(e, e1): mycursor.execute("UPDATE entries SET father=%s WHERE entryno=%s", (e1, e)); mydb.commit(); tmsg.showinfo("Message", "Entry updated successfully!")
def n5(e, e1): mycursor.execute("UPDATE entries SET nationality=%s WHERE entryno=%s", (e1, e)); mydb.commit(); tmsg.showinfo("Message", "Entry updated successfully!")
def n6(e, e1): mycursor.execute("UPDATE entries SET minority=%s WHERE entryno=%s", (e1, e)); mydb.commit(); tmsg.showinfo("Message", "Entry updated successfully!")
def n7(e, e1): mycursor.execute("UPDATE entries SET email=%s WHERE entryno=%s", (e1, e)); mydb.commit(); tmsg.showinfo("Message", "Entry updated successfully!")

def update():
    frame1 = Frame(root, bg='black', width=1000, height=500)
    frame1.place(relx=0.5, y=20, anchor='n')  # Top-center at y=20

    e = Entry(frame1, width=50)
    e.pack()
    e.insert(0, 'Enter your entry number')
    e.bind("<FocusIn>", lambda event: clear_placeholder(event, e, 'Enter your entry number'))

    def proceed():
        try:
            entry_no = int(e.get())
        except ValueError:
            tmsg.showerror("Error", "Please enter a valid entry number!")
            return

        mycursor.execute("SELECT * FROM entries WHERE entryno=%s", (entry_no,))
        data = mycursor.fetchall()
        if not data:
            tmsg.showinfo("Error", "Entry not found!")
            return

        # Inner function to create field update UI
        def update_field(field_name, label_text, update_func):
            sub_frame = Frame(frame1, bg='black')
            sub_frame.pack()

            e1 = Entry(sub_frame, width=50)
            e1.pack()
            e1.insert(0, f'Enter new {label_text}')
            e1.bind("<FocusIn>", lambda event: clear_placeholder(event, e1, f'Enter new {label_text}'))

            def call_update():
                value = e1.get()
                update_func(entry_no, value)
                sub_frame.destroy()

            Button(sub_frame, text="Submit Update", bg="#af4063", fg="#c8f0b1", command=call_update).pack()

        # Buttons for each field
        Button(frame1, text='Update Name', bg="#e9c67c", fg="#070d3d", command=lambda: update_field('name', 'Name', lambda e, v: n(e, v))).pack()
        Button(frame1, text='Update Age', bg="#e9c67c", fg="#070d3d", command=lambda: update_field('age', 'Age', lambda e, v: n1(e, v))).pack()
        Button(frame1, text='Update Gender', bg="#e9c67c", fg="#070d3d", command=lambda: update_field('gender', 'Gender', lambda e, v: n2(e, v))).pack()
        Button(frame1, text="Update Mother's Name", bg="#e9c67c", fg="#070d3d", command=lambda: update_field('mother', "Mother's Name", lambda e, v: n3(e, v))).pack()
        Button(frame1, text="Update Father's Name", bg="#e9c67c", fg="#070d3d", command=lambda: update_field('father', "Father's Name", lambda e, v: n4(e, v))).pack()
        Button(frame1, text='Update Nationality Status', bg="#e9c67c", fg="#070d3d", command=lambda: update_field('nationality', 'Nationality', lambda e, v: n5(e, v))).pack()
        Button(frame1, text='Update Minority Status', bg="#e9c67c", fg="#070d3d", command=lambda: update_field('minority', 'Minority', lambda e, v: n6(e, v))).pack()
        Button(frame1, text="Update Email ID", bg="#e9c67c", fg="#070d3d", command=lambda: update_field('email', 'Email', lambda e, v: n7(e, v))).pack()
        Button(frame1, text='Exit', font=('Helvetica', 18, 'bold'), width=20, bg="#32639e", fg="#c8f0b1", command=frame1.destroy).pack(anchor='center')

    Button(frame1, text='Submit', bg="#af4063", fg="#c8f0b1", command=lambda: [proceed(), e.destroy()]).pack()

# Delete an entry
def deleteget(e):
    try:
        entry_no = int(e.get())
    except ValueError:
        tmsg.showerror("Error", "Please enter a valid entry number!")
        return

    mycursor.execute("SELECT * FROM entries WHERE entryno=%s", (entry_no,))
    data = mycursor.fetchall()
    if data == []:
        tmsg.showinfo("Error", "Entry not found!")
    else:
        mycursor.execute("DELETE FROM entries WHERE entryno=%s", (entry_no,))
        mydb.commit()
        tmsg.showinfo("Message", "Entry deleted successfully!")

def delete():
    frame1 = Frame(root, bg='black', width=1000, height=500)
    frame1.place(relx=0.5, y=20, anchor='n')  # Top-center at y=20

    e = Entry(frame1, width=50)
    e.pack()
    e.insert(0, 'Enter your entry number')
    e.bind("<FocusIn>", lambda event: clear_placeholder(event, e, 'Enter your entry number'))
    Button(frame1, text='Submit',bg="#af4063",fg="#c8f0b1", command=lambda: [deleteget(e), frame1.destroy()]).pack()

# Button Design + Placement

button_width = 40
button_height = 2
button_bg = "#e652ab"
button_fg = "#7dc3e0"
button_font = ('Arial', 12, 'bold')
button_padx = 10
button_pady = 5

# All Buttons on UI
Button(text='Register for CDS examination', width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=button_font, padx=button_padx, pady=button_pady, command=insert).pack(anchor='nw', pady=20, padx=50)
Button(text='Display Entries', width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=button_font, padx=button_padx, pady=button_pady, command=display).pack(anchor='nw', pady=20, padx=50)
Button(text='Search an Entry', width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=button_font, padx=button_padx, pady=button_pady, command=search).pack(anchor='nw', pady=20, padx=50)
Button(text='Update an Entry', width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=button_font, padx=button_padx, pady=button_pady, command=update).pack(anchor='nw', pady=20, padx=50)
Button(text='Delete an Entry', width=button_width, height=button_height, bg=button_bg, fg=button_fg, font=button_font, padx=button_padx, pady=button_pady, command=delete).pack(anchor='nw', pady=20, padx=50)

# Start GUI main loop
root.mainloop()