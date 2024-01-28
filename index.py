print("Hello, World!")

# Variables
name = "John"
age = 25
height = 1.75
is_student = True

# Data types
print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(is_student))  # <class 'bool'>

# Lists
fruits = ["apple", "banana", "orange"]
print(*fruits)
print(fruits[0])    # apple
fruits.append("grape")
print(len(fruits))   # 4
print(fruits[-1])

# List of dictionaries
students = [{"name": "Bob", "age": 30, "is_student": False}, {"name": "Alice", "age": 25, "is_student": True}]
sum_of_ages = sum(student["age"] for student in students)
print("Avarage age:", sum_of_ages/len(students))

# For loop
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# If statement
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Dictionaries
person = {"name": "Bob", "age": 30, "is_student": False}
print(person["name"])  # Bob

# File handling
with open("output.txt", "w") as file:
    file.write("Hello, File!")

with open("output.txt", "r") as file:
    content = file.read()
    print(content)

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Classes and objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

my_dog = Dog("Buddy", 3)
print(my_dog.name)
my_dog.bark()
