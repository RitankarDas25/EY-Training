import json
import logging

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#1: Read and print all student names
try:
    with open('students.json', 'r') as file:
        students = json.load(file)
        logging.info("File read successful.")
except FileNotFoundError:
    logging.error("students.json file not found.")
    students = []

# Print all student names
print("Student Names:")
for student in students:
    print(student["name"])

#  2: Add new student
new_student = {
    "name": "Arjun",
    "age": 20,
    "course": "Data Science",
    "marks": 78
}
students.append(new_student)
logging.info("Student added: Arjun")

#  3: Save updated list back to JSON file
try:
    with open('students.json', 'w') as file:
        json.dump(students, file, indent=2)
        logging.info("Updated file saved successfully.")
except Exception as e:
    logging.error(f"Failed to save file: {e}")