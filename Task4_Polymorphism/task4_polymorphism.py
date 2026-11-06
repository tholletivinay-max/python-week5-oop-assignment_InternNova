
# TASK 4: POLYMORPHISM IN PYTHON

# First class
class Student:

    def display_details(self):
        print("Student Information")
        print("Name: Vinay")
        print("Roll Number: 101")
        print("Department: AI & Data Science")


# Second class
class Employee:

    def display_details(self):
        print("\nEmployee Information")
        print("Name: Arun")
        print("Employee ID: 201")
        print("Department: Software Development")


# Creating objects
student = Student()
employee = Employee()

# Calling the same method for different objects
print("POLYMORPHISM DEMONSTRATION")
print("============================")

student.display_details()
employee.display_details()
