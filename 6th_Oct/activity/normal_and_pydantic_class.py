#normal python class
class Student1:
    def __init__(self, name, age,email):
        self.name = name
        self.age = age
        self.email = email

data = {
    "name" : "John",
    "age" : "tewenty",
    "email" : "ygyuv"
}
student1 = Student1(**data)
print(student1.name)

#pydantic class
from pydantic import BaseModel

#define a model like a schema
class Student2(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool = True

# valid data
data={
    "name" : "John",
    "age" : 21,
    "email" : "ygyuv"
}
student2 = Student2(**data)

print(student2.name)

#invalid_data = {
#    "name" : "John",
#    "age" : "ten",
#    "email" : "ygyuv"
#}
#student = Student2(**invalid_data)
