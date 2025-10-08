from fastapi.testclient import TestClient
from employee import app

client = TestClient(app) #Arrange

#---------TEST 1-------
def test_get_all_employees():
    response = client.get("/employees") #ACT
    assert response.status_code == 200 #Assert
    assert isinstance(response.json(), dict) #Assert

# Arrange ACT Assert -- AAA Pattern
#CICD - Continuous Integration Continous Deployment -- checkin -- Build --Test Case-- Deployed to QA server
#-----TEST 2------
def test_add_employee():
    new_emp = {
        "id": 4,
        "name": "Neha Verma",
        "department": "Software Engineering",
        "salary": 20000,
    }
    response = client.post("/employees", json=new_emp)
    assert response.status_code == 201
    assert response.json()["name"] == "Neha Verma"

   # -----Test 3------
def test_get_employee_by_id():
    response = client.get("/employees/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Bob Johnson"

    #-----test 4------
def test_employee_not_found():
    response = client.get("/employees/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"

#-----test 5-------
def test_update_employee():
    new_emp = {
        "id": 2,
        "name": "Abhi",
        "department": "Software Engineering",
        "salary": 45000,
    }
    response = client.put("/employees/2", json=new_emp)
    assert response.status_code == 200
    assert response.json()["employee"]["name"] == "Abhi"

#-----test 6------
def test_delete_employee():
    response = client.delete("/employees/1")
    assert response.status_code == 200
    assert response.json()["employee"]["name"] == "Alice Smith"
