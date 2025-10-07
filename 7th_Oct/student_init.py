from fastapi import FastAPI

#create FastApi instance
app = FastAPI()

#root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI demo!"}

#path parameter example
@app.get("/students/{student_id}")
def read_student(student_id: int):
    return {"student_id": student_id,"name":"rahul","course":"AI"}