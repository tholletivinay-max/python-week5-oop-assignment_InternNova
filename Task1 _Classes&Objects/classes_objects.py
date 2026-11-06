
# TASK 1: CLASSES AND OBJECTS

# Creating a Student class
class Student:

    # Method to display student information
    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Department:", self.department)
        print("College:", self.college)
        print("----------------------------")


# Creating the first object
student1 = Student()
student1.name = "Vinay"
student1.roll_number = 101
student1.department = "AI & Data Science"
student1.college = "Dhanalakshmi Srinivasan University"

# Creating the second object
student2 = Student()
student2.name = "Arun"
student2.roll_number = 102
student2.department = "Computer Science"
student2.college = "Dhanalakshmi Srinivasan University"

# Displaying student details
print("STUDENT MANAGEMENT SYSTEM")
print("============================")

print("\nFirst Student Details:")
student1.display_details()

print("Second Student Details:")
student2.display_details()
