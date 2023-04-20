# --------------------------------------------Admin log in and registration----------------------

import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rku_attendence_admin"
)

# Create the main window
root = tk.Tk()

# Set the window title and size
root.title("RKU Student Attendance System")
root.geometry("500x400")

# Add a label with the university name
label = tk.Label(root, text="Welcome to RKU Attendance System",
                 font=("Arial", 20))
label.pack(pady=20)

# Add a label and entry for username
username_label = tk.Label(root, text="Username", font=("Arial", 14))
username_label.pack()
username_entry = tk.Entry(root, font=("Arial", 14))
username_entry.pack()

# Add a label and entry for password
password_label = tk.Label(root, text="Password", font=("Arial", 14))
password_label.pack()
password_entry = tk.Entry(root, show="*", font=("Arial", 14))
password_entry.pack()

# Add a button to log in as admin


def login():
    # Retrieve the values entered in the username and password entry fields
    username = username_entry.get()
    password = password_entry.get()

    # Query the MySQL database to check if the username and password match an admin account
    cursor = db.cursor()
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        status_label.config(text="Login successful", fg="green")
    else:
        status_label.config(text="Login failed", fg="red")


def login_as_admin():
    class Student:
        def __init__(self, name, roll, major):
            self.name = name
            self.roll = roll
            self.major = major

    class StudentRegistrationApp:
        def __init__(self, master):
            self.master = master
            master.title("RKU Attendance System")
            master.geometry("500x530")

            # Connect to the MySQL database
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="rku_attendence_admin"
            )
            self.cursor = self.db.cursor()

            # Create IT and CE student lists
            self.it_students = []
            self.ce_students = []

            # Create header frame and welcome label
            header_frame = tk.Frame(master)
            header_frame.pack(side=tk.TOP, pady=10)
            tk.Label(header_frame, text="Welcome to RKU Server",
                     font=("Arial", 16)).pack()

            # Create labels and entry fields for name, roll, and major
            tk.Label(master, text="Name").pack()
            self.name_entry = tk.Entry(master)
            self.name_entry.pack()

            tk.Label(master, text="Roll").pack()
            self.roll_entry = tk.Entry(master)
            self.roll_entry.pack()

            tk.Label(master, text="Major").pack()
            self.major_var = tk.StringVar(value="IT")
            self.major_dropdown = tk.OptionMenu(
                master, self.major_var, "IT", "CE")
            self.major_dropdown.pack()

            # Create button for registering student
            self.register_button = tk.Button(
                master, text="Register", command=self.register_student)
            self.register_button.pack(pady=10)
            # -------Start-----------------------------------#

            def take_attendance_callback_function():
                pass 
            # -------------------------------------end------#
            take_attendance_button = tk.Button(
                master, text="Take Attendance", command=take_attendance_callback_function)
            take_attendance_button.pack(pady=10)

            # Create reset button
            self.reset_button = tk.Button(
                master, text="Reset", command=self.reset_fields)
            self.reset_button.pack(pady=10)

            # Create label for displaying registered students
            tk.Label(master, text="Registered Students").pack()
            self.student_listbox = tk.Listbox(master)
            self.student_listbox.pack()

        def register_student(self):
            name = self.name_entry.get()
            roll = self.roll_entry.get()
            major = self.major_var.get()
            if major == "IT":
                student = Student(name, roll, "IT")
                self.it_students.append(student)
                # Store IT student data to the database
                query = "INSERT INTO it_students (name, roll) VALUES (%s, %s)"
                values = (name, roll)
                self.cursor.execute(query, values)
                self.db.commit()
            else:
                student = Student(name, roll, "CE")
                self.ce_students.append(student)
                # Store CE student data to the database
                query = "INSERT INTO ce_students (name, roll) VALUES (%s, %s)"
                values = (name, roll)
                self.cursor.execute(query, values)
                self.db.commit()
            self.student_listbox.delete(0, tk.END)
            for student in self.it_students + self.ce_students:
                self.student_listbox.insert(
                    tk.END, f"{student.name} ({student.major}) - Roll No. {student.roll}")
            # Show success message
            messagebox.showinfo("Success", "Student registered successfully!")

        def reset_fields(self):
            self.name_entry.delete(0, tk.END)
            self.roll_entry.delete(0, tk.END)
            self.major_var.set("IT")
            self.student_listbox.delete

    root = tk.Tk()
    app = StudentRegistrationApp(root)
    root.mainloop()


login_button = tk.Button(root, text="Login as Admin", font=(
    "Arial", 16), width=20, height=2, command=login_as_admin)
login_button.pack(pady=10)

# Add a button to register as admin


def register():
    # Retrieve the values entered in the username and password entry fields
    username = username_entry.get()
    password = password_entry.get()

    # Insert a new admin account into the MySQL database
    cursor = db.cursor()
    query = "INSERT INTO admin (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    db.commit()

    status_label.config(text="Registration successful", fg="green")


register_button = tk.Button(root, text="Register as Admin", font=(
    "Arial", 16), width=20, height=2, command=register)
register_button.pack(pady=10)

# Add a label to display the login/registration status
status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack(pady=10)

# Add a button to reset the username and password entry fields


def reset():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


reset_button = tk.Button(root, text="Reset", font=(
    "Arial", 12), width=10, command=reset)
reset_button.pack(pady=10)

# Run the main event loop
root.mainloop()

# Close the database connection
db.close()
