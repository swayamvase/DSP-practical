# -------------------------
# Tuple Operations
# -------------------------
t = (10, 20, 30, 40)

print("Tuple element:", t[1])


# -------------------------
# Set Operations
# -------------------------
s = {1, 2, 3, 4}

s.add(5)
s.remove(2)

print("Set:", s)


# -------------------------
# Dictionary Operations
# -------------------------
student = {
    "name": "Amit",
    "age": 20,
    "marks": 85
}

# Accessing values
print("Name:", student["name"])

# Updating values
student["marks"] = 90

# Adding a new key-value pair
student["city"] = "Nagpur"

# Deleting a key-value pair
del student["age"]

print("Updated Dictionary:", student)

# Built-in dictionary methods
print("Dictionary keys:", student.keys())
print("Dictionary values:", student.values())
print("Dictionary items:", student.items())