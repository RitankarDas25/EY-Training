from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI()

# Pydantic model for validation
class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float

# In-memory employee list with 3 sample employees
employees = [
    {"id": 1, "name": "Alice Smith", "department": "HR", "salary": 50000},
    {"id": 2, "name": "Bob Johnson", "department": "IT", "salary": 65000},
    {"id": 3, "name": "Charlie Brown", "department": "Marketing", "salary": 55000},
]

# GET: Return all employees
@app.get("/employees")
def get_all_employees():
    return {"employees": employees}

# GET: Return single employee by ID
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# POST: Add a new employee
@app.post("/employees", status_code=201)
def add_employee(new_emp: Employee):
    # Check for duplicate ID
    for emp in employees:
        if emp["id"] == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employees.append(new_emp.dict())
    return {"message": "Employee added successfully", "employee": new_emp}

# PUT: Update existing employee
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, updated_emp: Employee):
    if emp_id != updated_emp.id:
        raise HTTPException(status_code=400, detail="ID in path and body do not match")

    for i, emp in enumerate(employees):
        if emp["id"] == emp_id:
            employees[i] = updated_emp.dict()
            return {"message": "Employee updated successfully", "employee": updated_emp}
    raise HTTPException(status_code=404, detail="Employee not found")

# DELETE: Remove employee by ID
@app.delete("/employees/{emp_id}", status_code=200)
def delete_employee(emp_id: int):
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            return {"message": "Employee deleted successfully", "employee": emp}
    raise HTTPException(status_code=404, detail="Employee not found")

# BONUS: Get total count of employees
@app.get("/employees/count")
def get_employee_count():
    return {"count": len(employees)}
