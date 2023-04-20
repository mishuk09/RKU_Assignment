import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Establishing connection with the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rku_attendence_admin"
)

# Creating a cursor object
mycursor = mydb.cursor()
student_data = None
division_name_table = None
attendance_status_boolean = []

# Defining the function to display the student data with tick marks for attendance


def display_attendance(table_name):
    global attendance_status_boolean, student_data
    # Fetching the student data from the table
    mycursor.execute("SELECT * FROM " + table_name)
    student_data = mycursor.fetchall()

    # Defining the function to update attendance status
    def update_attendance_status(i, value):
        attendance_status_boolean[i] = value

    # Clearing the previous data from the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Creating the table headers
    headers = ["Roll No.", "Name", "Attendance"]
    for j, header in enumerate(headers):
        label = tk.Label(frame, text=header)
        label.grid(row=0, column=j)

    # Creating a table to display the student data with tick marks for attendance
    for i in range(len(student_data)):
        # Displaying the roll number
        label = tk.Label(frame, text=str(student_data[i][0]))
        label.grid(row=i+1, column=0)

        # Displaying the name
        label = tk.Label(frame, text=str(student_data[i][1]))
        label.grid(row=i+1, column=1)

        # Creating a checkbox to mark attendance
        attendance_var = tk.BooleanVar()
        attendance_var.set(False)
        attendance_checkbox = tk.Checkbutton(
            frame, variable=attendance_var, command=lambda i=i, v=attendance_var.get(): update_attendance_status(i, v))
        attendance_checkbox.grid(row=i+1, column=2)
        attendance_status_boolean.append(False)  # set initial value to False

# Defining the function to handle the submission of attendance data


def submit_attendance():
    # Getting the faculty, division, and date
    global attendance_status_boolean, student_data, division_name_table
    faculty = faculty_entry.get()
    division = dropdown_var.get()
    date = date_entry.get()

    # Creating a list of tuples containing student data and attendance status
    final_status = list(zip(student_data, attendance_status_boolean))

    # Inserting attendance data into the database
    for query in final_status:
        try:
            id = query[0][0]
            name = query[0][1]
            if False in query:
                query = f"INSERT INTO attendance VALUES ('{faculty}', '{division}', '{date}', '{name}','{id}', 'Absent');"
                mycursor.execute(query)
                mydb.commit()
            elif True in query:
                query = f"INSERT INTO attendance VALUES ('{faculty}', '{division}', '{date}', '{name}','{id}', 'Present');"
                mycursor.execute(query)
                mydb.commit()
        except Exception:
            messagebox.showerror("Error", "Error Occured")
            return
    messagebox.showinfo("Success", "Attendance Updated Successfully")

# Defining the function to handle the selection from the dropdown menu


def handle_dropdown(selection):
    global division_name_table
    if selection == "IT":
        display_attendance("it_students")
        division_name_table = "it_students"
    elif selection == "CE":
        display_attendance("ce_students")
        division_name_table = "ce_students"


    # Creating the Tkinter window
root = tk.Tk()
root.title("RKU Attendance")
root.geometry("500x400")

# Adding the RKU server label
rku_server_label = tk.Label(
    root, text="Welcome to RKU Server", font=("Arial", 20))
rku_server_label.pack()

faculty_frame = tk.Frame(root)
faculty_frame.pack()
faculty_label = tk.Label(faculty_frame, text="Faculty:")
faculty_label.pack(side="left", anchor="w")
faculty_entry = tk.Entry(faculty_frame)
faculty_entry.pack(side="left")

# Creating the Date label and entry
date_frame = tk.Frame(root)
date_frame.pack()
date_label = tk.Label(date_frame, text="Date:")
date_label.pack(side="left", anchor="w")
date_entry = tk.Entry(date_frame)
date_entry.pack(side="left")


# Creating a frame for the label and dropdown menu
dropdown_frame = tk.Frame(root)
dropdown_frame.pack()

# Creating the label for the dropdown menu
division_label = tk.Label(dropdown_frame, text="Division:")
division_label.pack(side="left", anchor="w")

# Creating the dropdown menu for IT and CE
options = ["IT", "CE"]
dropdown_var = tk.StringVar(root)
dropdown_var.set(options[0])
dropdown_menu = tk.OptionMenu(
    dropdown_frame, dropdown_var, *options, command=handle_dropdown)
dropdown_menu.pack(side="left")

# Creating a frame to display the data
frame = tk.Frame(root)
frame.pack()


# Creating the submit button
submit_button = tk.Button(
    root, text="Submit Attendance", command=submit_attendance)
submit_button.pack()


# Starting the Tkinter main loop
root.mainloop()
