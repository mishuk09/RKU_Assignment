import tkinter as tk
import mysql.connector

# Create a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="rku_attendence_admin"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Create a table if it does not already exist
mycursor.execute("CREATE TABLE IF NOT EXISTS attendance (id INT AUTO_INCREMENT PRIMARY KEY, faculty VARCHAR(255), division VARCHAR(255), date VARCHAR(255), student_name VARCHAR(255), attendance_status VARCHAR(255))")


class AttendanceGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("RKU Attendance System")

        # Create the welcome label
        welcome_label = tk.Label(
            self.root, text="Welcome to RKU Server", font=("Arial", 14))
        welcome_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Create input fields for faculty, division, and date
        faculty_label = tk.Label(self.root, text="Faculty:")
        faculty_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.faculty_entry = tk.Entry(self.root)
        self.faculty_entry.grid(row=1, column=1, padx=10, pady=10)

        division_label = tk.Label(self.root, text="Division:")
        division_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.division_entry = tk.Entry(self.root)
        self.division_entry.grid(row=2, column=1, padx=10, pady=10)

        date_label = tk.Label(self.root, text="Date:")
        date_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.date_entry = tk.Entry(self.root)
        self.date_entry.grid(row=3, column=1, padx=10, pady=10)

        # Create the headers for roll, name, and attendance
        roll_label = tk.Label(self.root, text="Roll")
        roll_label.grid(row=4, column=0, padx=10, pady=10)

        name_label = tk.Label(self.root, text="Name")
        name_label.grid(row=4, column=1, padx=10, pady=10)

        attendance_label = tk.Label(self.root, text="Attendance")
        attendance_label.grid(row=4, column=2, padx=10, pady=10)

        # Create the student labels, roll numbers, and tick mark buttons
        self.student_labels = []
        self.roll_labels = []
        self.tick_buttons = []
        for i in range(10):
            roll = i+1
            roll_label = tk.Label(self.root, text=roll)
            roll_label.grid(row=i+5, column=0, padx=10, pady=10)
            self.roll_labels.append(roll_label)

            name_label = tk.Label(self.root, text=f"Student {i+1}")
            name_label.grid(row=i+5, column=1, padx=10, pady=10)
            self.student_labels.append(name_label)

            tick_var = tk.BooleanVar()
            button = tk.Checkbutton(self.root, variable=tick_var)
            button.grid(row=i+5, column=2)
            self.tick_buttons.append(tick_var)

        # Create the submit button
        submit_button = tk.Button(
            self.root, text="Submit", command=self.submit_attendance)
        submit_button.grid(row=16, column=0, columnspan=3, padx=10, pady=10)

    def submit_attendance(self):
        # Get the attendance data from the input fields and tick marks
        faculty = self.faculty_entry.get()
        division = self.division_entry.get()
        date = self.date_entry.get()
        attendance_data = []
        for i, tick_var in enumerate(self.tick_buttons):
            roll = i+1
            name = self.student_labels[i].cget("text")
            attendance_status = "Present" if tick_var.get() else "Absent"
            attendance_data.append(
                (faculty, division, date, name, attendance_status))

        # Insert the attendance data into the database
        sql = "INSERT INTO attendance (faculty, division, date, student_name, attendance_status) VALUES (%s, %s, %s, %s, %s)"
        mycursor.executemany(sql, attendance_data)
        mydb.commit()

        # Show a message in the GUI interface
        message_label = tk.Label(
            self.root, text="Attendance data inserted successfully", fg="green")
        message_label.grid(row=17, column=0, columnspan=3, pady=10)


if __name__ == "__main__":
    app = AttendanceGUI()
    app.root.mainloop()
