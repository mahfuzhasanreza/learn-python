import sqlite3

def connect():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        cgpa REAL
    )
    """)
    conn.commit()
    conn.close()

def add_student():
    name = input("Name: ")
    age = int(input("Age: "))
    cgpa = float(input("CGPA: "))

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age, cgpa) VALUES (?, ?, ?)",
                (name, age, cgpa))
    conn.commit()
    conn.close()
    print("Student added!\n")

def view_students():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()

    for row in rows:
        print(row)
    print()

def update_student():
    student_id = int(input("Student ID: "))
    new_cgpa = float(input("New CGPA: "))

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("UPDATE students SET cgpa=? WHERE id=?", 
                (new_cgpa, student_id))
    conn.commit()
    conn.close()
    print("Updated!\n")

def delete_student():
    student_id = int(input("Student ID: "))

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()
    print("Deleted!\n")

def menu():
    connect()
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student CGPA")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        else:
            break

menu()
