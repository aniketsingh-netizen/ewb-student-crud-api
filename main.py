from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import sqlite3

app = FastAPI(title="Student Database CRUD API")

# Database Initialization
def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dob TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            course TEXT,
            address TEXT,
            enrollment_date TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Pydantic Models for Validation
class StudentCreate(BaseModel):
    name: str
    dob: str
    email: Optional[str] = None
    phone: Optional[str] = None
    course: Optional[str] = None
    address: Optional[str] = None
    enrollment_date: Optional[str] = None

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    dob: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    course: Optional[str] = None
    address: Optional[str] = None
    enrollment_date: Optional[str] = None

# 1. Create a Student
@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO students (name, dob, email, phone, course, address, enrollment_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (student.name, student.dob, student.email, student.phone, student.course, student.address, student.enrollment_date))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return {"message": "Student created successfully", "student_id": student_id, **student.dict()}

# 2. List / Filter Students
@app.get("/students")
def get_students(course: Optional[str] = None):
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if course:
        cursor.execute("SELECT * FROM students WHERE course = ?", (course,))
    else:
        cursor.execute("SELECT * FROM students")
        
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# 3. View a Single Student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="Student not found")
    return dict(row)

# 4. Update Student Details
@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Student not found")
        
    update_data = {k: v for k, v in student.dict().items() if v is not None}
    if not update_data:
        conn.close()
        return {"message": "No updates provided"}
        
    set_clause = ", ".join([f"{k} = ?" for k in update_data.keys()])
    values = list(update_data.values()) + [student_id]
    
    cursor.execute(f"UPDATE students SET {set_clause} WHERE student_id = ?", values)
    conn.commit()
    conn.close()
    return {"message": "Student updated successfully"}

# 5. Delete a Student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Student not found")
        
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()
    return {"message": "Student deleted successfully"}
