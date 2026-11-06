
# TASK 2: CONSTRUCTORS IN PYTHON

# Creating a Student class
class Student:

    # Constructor
    def __init__(self, name, roll_number, department, college):
        self.name = name
        self.roll_number = roll_number
        self.department = department
        self.college = college

    # Method to display student information
    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Department:", self.department)
        print("College:", self.college)
        print("----------------------------")


# Creating objects with different values
student1 = Student(
    "Vinay",
    101,
    "AI & Data Science",
    "Dhanalakshmi Srinivasan University"
)

student2 = Student(
    "Arun",
    102,
    "Computer Science",
    "Dhanalakshmi Srinivasan University"
)

# Accessing initialized attributes
print("STUDENT MANAGEMENT SYSTEM")
print("============================")

print("\nFirst Student Details:")
student1.display_details()

print("Second Student Details:")
student2.display_details()
