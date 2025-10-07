from fastapi import FastAPI

#create FastApi instance
app = FastAPI()

#root endpoint
#get
@app.get("/students")
def get_students():
    return {"this is a get request"}

#post method
@app.post("/students")
def create_student():
    return {"this is post request"}

# put method
@app.put("/students")
def update_student(s):
    return("this is a put request")

#delete method
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return("this is a delete request")