students={"Rahul","arjun","Rahul"}# no duplicates allowed in sets
students2={"priya","Rahul"}

print(students)
print("Rahul" in students) #returns true
print("Raj" in students) # returns false

print(students | students2) #union
print(students & students2) #intersection
print(students - students2) #difference

names=["Rahul","arjun","Rahul"]
unique_names=set(names) #list to set
print(unique_names)