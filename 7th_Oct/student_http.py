from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI()

# Pydantic model for validation
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

# In-memory database
students = [
    {"id": 1, "name": "Abhi", "age": 21, "course": "Python"},
    {"id": 2, "name": "Bella", "age": 22, "course": "AI"},
]

# GET all students
@app.get("/students")
def get_all_students():
    return {"students": students}

# GET a particular student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for s in students:
        if s["id"] == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")

# POST method to add a new student
@app.post("/students", status_code=201)
def add_student(new_student: Student):
    students.append(new_student.dict())
    return {"message": "Student added successfully", "student": new_student}


# put method to update student
@app.put("/students/{student_id}", status_code=200)
def update_student(student_id: int, updated_student: Student):
    for i,s in enumerate(students):
        if s["id"] == student_id:
            students[i] = updated_student.dict()
            return {"message": "Student updated successfully", "student": updated_student}
    raise HTTPException(status_code=404, detail="Student not found")

# delete method
@app.delete("/students/{student_id}",status_code=204)
def delete_student(student_id: int):
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            return {"message": "Student deleted successfully", "student": s}
    raise HTTPException(status_code=404, detail="Student not found")

