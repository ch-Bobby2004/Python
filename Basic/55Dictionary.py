students = {
    "101": {"name": "Rahul", "age": 20, "course": "Python"},
    "102": {"name": "Amit", "age": 22, "course": "Java"},
    "103": {"name": "Sita", "age": 19, "course": "C++"}
}

# Accessing data
print(students["101"]["name"])   # Rahul
print(students["102"]["course"]) # Java




students = {
    "101": {"name": "Rahul", "age": 20, "course": "Python"},
    "102": {"name": "Amit", "age": 22, "course": "Java"}
}

# Function to add a new student
def add_student(student_id, name, age, course):
    students[student_id] = {"name": name, "age": age, "course": course}
    print(f"Student {name} added successfully!")


add_student("103", "Sita", 19, "C++")


print(students)