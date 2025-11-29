import sqlite3

def insert_student(name, age, cgpa):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO students (name, age, cgpa) VALUES (?, ?, ?)",
                (name, age, cgpa))

    conn.commit()
    conn.close()
    print("Student added!")
    

insert_student("Aisha", 21, 3.5)
insert_student("Rahim", 24, 3.2)
insert_student("Karim", 22, 3.8)


def read_students():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()

    conn.close()
    return rows


print(read_students())


def update_cgpa(student_id, new_cgpa):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("UPDATE students SET cgpa = ? WHERE id = ?",
                (new_cgpa, student_id))

    conn.commit()
    conn.close()
    print("CGPA updated!")
    

update_cgpa(1, 3.9)


def delete_student(student_id):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))

    conn.commit()
    conn.close()
    print("Student deleted!")
    

delete_student(2)
