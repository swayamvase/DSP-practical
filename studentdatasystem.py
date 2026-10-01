# Student Data System
# Demonstrates Python building blocks, data types, and I/O

print("=== Student Data System ===")

# Input section
name = input("Enter student name: ")          # str
roll_no = int(input("Enter roll number: "))    # int
age = int(input("Enter age: "))               # int
marks = float(input("Enter marks: "))         # float

# Boolean expression
is_pass = marks >= 40                         # bool

# Processing section
percentage = (marks / 100) * 100

# Output section
print("\n=== Student Details ===")
print("Name:", name)
print("Roll Number:", roll_no)
print("Age:", age)
print("Marks:", marks)
print("Percentage:", percentage)
print("Result:", "Pass" if is_pass else "Fail")

# Display data types
print("\n=== Data Types Used ===")
print("Type of name:", type(name))
print("Type of roll_no:", type(roll_no))
print("Type of age:", type(age))
print("Type of marks:", type(marks))
print("Type of is_pass:", type(is_pass))