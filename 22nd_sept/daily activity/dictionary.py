#creating dictionary
student ={
    "name":"Ritankar",
    "age":22,
    "course":"aiml"

}
#acessing value by key
print(student["name"])
print(student.get("age"))

student["grade"]= "A" #adding key value pair
student["age"]= 25 #updating value
print(student)

student.pop("course") #remove by key
del student["grade"] #delete key
print(student)

for key,value in student.items(): #unpacking dictionary
    print(key,":",value)

employee={
    "name":"Ritankar",
    "age":22,
    "skills":["python","java","power BI"],

}
print(employee["skills"][1]) #acessing nested elements