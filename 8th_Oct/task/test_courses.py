from fastapi.testclient import TestClient
from courses_api import app

client = TestClient(app) #Arrange

#---------TEST 1-------
def test_add_course():
    new_course = {
        "id": 2,
        "title": "AIML",
        "duration": 20,
        "fee": 20000,
        "is_active": True,
    }
    response = client.post("/courses", json=new_course)
    assert response.status_code == 201
    assert response.json()["title"] == "AIML"

#----test 2-----
def test_add_course_already_exists():
    new_course = {
        "id": 2,
        "title": "AIML",
        "duration": 20,
        "fee": 20000,
        "is_active": True,
    }
    response = client.post("/courses", json=new_course)
    assert response.status_code == 400
    assert response.json()["detail"] == "Course ID already exists"

#------test 3-----
def test_invalid_duration_fee():
    new_course = {
        "id": 2,
        "title": "AIML",
        "duration": 0,
        "fee": -500,
        "is_active": True
    }
    response = client.post("/courses", json=new_course)
    assert response.status_code == 422
    response_text = response.text

    # Check that validation errors mention "not_gt" (not greater than)
    assert "greater_than" in response_text

#----TEST 4------
def test_get_all_courses():
    response = client.get("/courses")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all("id" in course for course in data)
    assert all("title" in course for course in data)
    assert all("duration" in course for course in data)
    assert all("fee" in course for course in data)


