import tkinter as tk
import mysql.connector
from tkinter import messagebox

root = tk.Tk()
root.title("Student Lists")
root.geometry("400x800")
check_box_values = None
# faculty entry label
faculty_label = tk.Label(root, text="Faculty Name: ")
faculty_label.place(x=100, y=20)
faculty_entry = tk.Entry(root)
faculty_entry.place(x=200, y=20)
# date label
date_label = tk.Label(root, text="Select Date")
date_label.place(x=100, y=45)
select_date_entry = tk.Entry(root)
select_date_entry.place(x=200, y=45)
# date_label.pack()

# division combobox
select_division_label = tk.Label(root, text="Select Division")
select_division_label.place(x=100, y=70)
select_division = tk.StringVar()

division_combobox = tk.OptionMenu(
    root, variable=select_division, value=("CE"))
division_combobox.place(x=200, y=70)
# get student button


def get_details():
    global check_box_values
    try:
        connection = mysql.connector.connect(
            host="localhost", username="root", password="", database="rku_attendence_admin")
        cursor = connection.cursor()
        query = "Select * from ce"
        cursor.execute(query)
        student_data_from_db = cursor.fetchall()
        start = 130
        # print(student_data_from_db[0])
        check_box_values = []
        for i in range(0, len(student_data_from_db)):
            student_lables = tk.Label(root, text=student_data_from_db[i])
            student_lables.place(x=190, y=start)
            check_box = tk.Checkbutton(root)
            check_box.place(x=270, y=start)
            start += 20
            check_box_values.append(check_box)
    except:
        messagebox.showerror("Error", "Couldnot Connect to Database")


get_student_button = tk.Button(
    root, text="Student Details", command=get_details)
get_student_button.place(x=200, y=100)


def update():
    global check_box_values
    final_check = []
    for i in check_box_values:
        value = i.instate(['selected'])
        final_check.append(value)
    print(final_check)


update_attendace_btn = tk.Button(
    root, text="Update Attendance", command=update)
update_attendace_btn.place(x=160, y=600)


root.mainloop()
